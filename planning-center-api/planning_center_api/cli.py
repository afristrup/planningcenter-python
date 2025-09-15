"""Command-line interface for Planning Center API."""

import asyncio
import json
import sys
from pathlib import Path
from typing import Any

import click
from click import Context

from .client import PCOClient
from .config import PCOConfig, PCOProduct
from .exceptions import PCOError


@click.group()
@click.option(
    "--app-id",
    envvar="PCO_APP_ID",
    help="Planning Center application ID",
)
@click.option(
    "--secret",
    envvar="PCO_SECRET",
    help="Planning Center application secret",
)
@click.option(
    "--access-token",
    envvar="PCO_ACCESS_TOKEN",
    help="Planning Center OAuth access token",
)
@click.option(
    "--config-file",
    type=click.Path(exists=True, path_type=Path),
    help="Configuration file path",
)
@click.pass_context
def cli(
    ctx: Context,
    app_id: str | None,
    secret: str | None,
    access_token: str | None,
    config_file: Path | None,
):
    """Planning Center API CLI tool."""
    # Load configuration
    config = PCOConfig()

    if config_file:
        config_data = json.loads(config_file.read_text())
        config = PCOConfig(**config_data)
    else:
        if app_id:
            config.app_id = app_id
        if secret:
            config.secret = secret
        if access_token:
            config.access_token = access_token

    ctx.ensure_object(dict)
    ctx.obj["config"] = config


@cli.command()
@click.option(
    "--product", type=click.Choice([p.value for p in PCOProduct]), required=True
)
@click.option(
    "--resource", required=True, help="Resource type (e.g., people, services)"
)
@click.option("--id", help="Specific resource ID")
@click.option("--per-page", type=int, help="Number of items per page")
@click.option("--offset", type=int, help="Offset for pagination")
@click.option("--include", help="Comma-separated list of related resources to include")
@click.option("--filter", help="Filter parameters as JSON")
@click.option("--sort", help="Sort order")
@click.option("--output", type=click.Choice(["json", "table", "csv"]), default="json")
@click.pass_context
def get(
    ctx: Context,
    product: str,
    resource: str,
    id: str | None,
    per_page: int | None,
    offset: int | None,
    include: str | None,
    filter: str | None,
    sort: str | None,
    output: str,
):
    """Get resources from Planning Center API."""

    async def _get():
        config = ctx.obj["config"]
        product_enum = PCOProduct(product)

        include_list = include.split(",") if include else None
        filter_params = json.loads(filter) if filter else None

        async with PCOClient(config=config) as client:
            try:
                result = await client.get(
                    product=product_enum,
                    resource=resource,
                    resource_id=id,
                    per_page=per_page,
                    offset=offset,
                    include=include_list,
                    filter_params=filter_params,
                    sort=sort,
                )

                if output == "json":
                    click.echo(json.dumps(result.model_dump(), indent=2, default=str))
                elif output == "table":
                    _print_table(result)
                elif output == "csv":
                    _print_csv(result)

            except PCOError as e:
                click.echo(f"Error: {e.message}", err=True)
                sys.exit(1)

    asyncio.run(_get())


@cli.command()
@click.option(
    "--product", type=click.Choice([p.value for p in PCOProduct]), required=True
)
@click.option("--resource", required=True, help="Resource type")
@click.option("--data", required=True, help="Resource data as JSON")
@click.option("--include", help="Comma-separated list of related resources to include")
@click.pass_context
def create(
    ctx: Context,
    product: str,
    resource: str,
    data: str,
    include: str | None,
):
    """Create a new resource in Planning Center API."""

    async def _create():
        config = ctx.obj["config"]
        product_enum = PCOProduct(product)

        include_list = include.split(",") if include else None
        data_dict = json.loads(data)

        async with PCOClient(config=config) as client:
            try:
                result = await client.create(
                    product=product_enum,
                    resource=resource,
                    data=data_dict,
                    include=include_list,
                )
                click.echo(json.dumps(result.model_dump(), indent=2, default=str))
            except PCOError as e:
                click.echo(f"Error: {e.message}", err=True)
                sys.exit(1)

    asyncio.run(_create())


@cli.command()
@click.option(
    "--product", type=click.Choice([p.value for p in PCOProduct]), required=True
)
@click.option("--resource", required=True, help="Resource type")
@click.option("--id", required=True, help="Resource ID")
@click.option("--data", required=True, help="Updated resource data as JSON")
@click.option("--include", help="Comma-separated list of related resources to include")
@click.pass_context
def update(
    ctx: Context,
    product: str,
    resource: str,
    id: str,
    data: str,
    include: str | None,
):
    """Update a resource in Planning Center API."""

    async def _update():
        config = ctx.obj["config"]
        product_enum = PCOProduct(product)

        include_list = include.split(",") if include else None
        data_dict = json.loads(data)

        async with PCOClient(config=config) as client:
            try:
                result = await client.update(
                    product=product_enum,
                    resource=resource,
                    resource_id=id,
                    data=data_dict,
                    include=include_list,
                )
                click.echo(json.dumps(result.model_dump(), indent=2, default=str))
            except PCOError as e:
                click.echo(f"Error: {e.message}", err=True)
                sys.exit(1)

    asyncio.run(_update())


@cli.command()
@click.option(
    "--product", type=click.Choice([p.value for p in PCOProduct]), required=True
)
@click.option("--resource", required=True, help="Resource type")
@click.option("--id", required=True, help="Resource ID")
@click.pass_context
def delete(
    ctx: Context,
    product: str,
    resource: str,
    id: str,
):
    """Delete a resource from Planning Center API."""

    async def _delete():
        config = ctx.obj["config"]
        product_enum = PCOProduct(product)

        async with PCOClient(config=config) as client:
            try:
                success = await client.delete(
                    product=product_enum,
                    resource=resource,
                    resource_id=id,
                )
                if success:
                    click.echo("Resource deleted successfully")
                else:
                    click.echo("Failed to delete resource", err=True)
                    sys.exit(1)
            except PCOError as e:
                click.echo(f"Error: {e.message}", err=True)
                sys.exit(1)

    asyncio.run(_delete())


@cli.command()
@click.option(
    "--product", type=click.Choice([p.value for p in PCOProduct]), required=True
)
@click.option("--resource", required=True, help="Resource type")
@click.option("--per-page", type=int, default=25, help="Number of items per page")
@click.option("--include", help="Comma-separated list of related resources to include")
@click.option("--filter", help="Filter parameters as JSON")
@click.option("--sort", help="Sort order")
@click.option("--output", type=click.Choice(["json", "table", "csv"]), default="json")
@click.pass_context
def paginate(
    ctx: Context,
    product: str,
    resource: str,
    per_page: int,
    include: str | None,
    filter: str | None,
    sort: str | None,
    output: str,
):
    """Paginate through all resources of a type."""

    async def _paginate():
        config = ctx.obj["config"]
        product_enum = PCOProduct(product)

        include_list = include.split(",") if include else None
        filter_params = json.loads(filter) if filter else None

        async with PCOClient(config=config) as client:
            try:
                results = []
                async for item in client.paginate_all(
                    product=product_enum,
                    resource=resource,
                    per_page=per_page,
                    include=include_list,
                    filter_params=filter_params,
                    sort=sort,
                ):
                    results.append(item)

                if output == "json":
                    click.echo(
                        json.dumps(
                            [r.model_dump() for r in results], indent=2, default=str
                        )
                    )
                elif output == "table":
                    _print_table(results)
                elif output == "csv":
                    _print_csv(results)

            except PCOError as e:
                click.echo(f"Error: {e.message}", err=True)
                sys.exit(1)

    asyncio.run(_paginate())


@cli.command()
@click.option("--query", required=True, help="Search query")
@click.option("--per-page", type=int, help="Number of items per page")
@click.option("--include", help="Comma-separated list of related resources to include")
@click.option("--output", type=click.Choice(["json", "table", "csv"]), default="json")
@click.pass_context
def search_people(
    ctx: Context,
    query: str,
    per_page: int | None,
    include: str | None,
    output: str,
):
    """Search for people by name or email."""

    async def _search():
        config = ctx.obj["config"]

        include_list = include.split(",") if include else None

        async with PCOClient(config=config) as client:
            try:
                result = await client.search_people(
                    query=query,
                    per_page=per_page,
                    include=include_list,
                )

                if output == "json":
                    click.echo(json.dumps(result.model_dump(), indent=2, default=str))
                elif output == "table":
                    _print_table(result)
                elif output == "csv":
                    _print_csv(result)

            except PCOError as e:
                click.echo(f"Error: {e.message}", err=True)
                sys.exit(1)

    asyncio.run(_search())


@cli.command()
@click.option("--email", required=True, help="Email address")
@click.option("--include", help="Comma-separated list of related resources to include")
@click.option("--output", type=click.Choice(["json", "table", "csv"]), default="json")
@click.pass_context
def find_by_email(
    ctx: Context,
    email: str,
    include: str | None,
    output: str,
):
    """Find people by email address."""

    async def _find():
        config = ctx.obj["config"]

        include_list = include.split(",") if include else None

        async with PCOClient(config=config) as client:
            try:
                result = await client.get_people_by_email(
                    email=email,
                    include=include_list,
                )

                if output == "json":
                    click.echo(json.dumps(result.model_dump(), indent=2, default=str))
                elif output == "table":
                    _print_table(result)
                elif output == "csv":
                    _print_csv(result)

            except PCOError as e:
                click.echo(f"Error: {e.message}", err=True)
                sys.exit(1)

    asyncio.run(_find())


def _print_table(data: Any) -> None:
    """Print data in table format."""
    if hasattr(data, "data") and isinstance(data.data, list):
        # Collection
        if not data.data:
            click.echo("No data found")
            return

        # Get all unique keys from all items
        all_keys = set()
        for item in data.data:
            all_keys.update(item.attributes.keys())

        # Print header
        headers = ["ID", "Type"] + sorted(all_keys)
        click.echo("\t".join(headers))

        # Print rows
        for item in data.data:
            row = [item.id, item.type]
            for key in sorted(all_keys):
                value = item.attributes.get(key, "")
                row.append(str(value))
            click.echo("\t".join(row))
    else:
        # Single item
        click.echo(f"ID: {data.id}")
        click.echo(f"Type: {data.type}")
        for key, value in data.attributes.items():
            click.echo(f"{key}: {value}")


def _print_csv(data: Any) -> None:
    """Print data in CSV format."""
    if hasattr(data, "data") and isinstance(data.data, list):
        # Collection
        if not data.data:
            click.echo("No data found")
            return

        # Get all unique keys from all items
        all_keys = set()
        for item in data.data:
            all_keys.update(item.attributes.keys())

        # Print header
        headers = ["ID", "Type"] + sorted(all_keys)
        click.echo(",".join(f'"{h}"' for h in headers))

        # Print rows
        for item in data.data:
            row = [item.id, item.type]
            for key in sorted(all_keys):
                value = item.attributes.get(key, "")
                # Escape quotes and wrap in quotes
                escaped_value = str(value).replace('"', '""')
                row.append(f'"{escaped_value}"')
            click.echo(",".join(row))
    else:
        # Single item
        click.echo(f"ID,Type,{','.join(data.attributes.keys())}")
        row = [data.id, data.type] + [str(v) for v in data.attributes.values()]
        click.echo(",".join(f'"{v}"' for v in row))


if __name__ == "__main__":
    cli()
