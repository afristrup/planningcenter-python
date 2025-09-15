"""Giving product models for Planning Center API."""

from datetime import datetime
from decimal import Decimal

from ..models.base import PCOResource


class PCODonation(PCOResource):
    """Represents a donation in Planning Center Giving."""

    def get_amount(self) -> Decimal | None:
        """Get the donation amount."""
        amount = self.get_attribute("amount")
        if amount is not None:
            return Decimal(str(amount))
        return None

    def get_currency(self) -> str | None:
        """Get the donation currency."""
        return self.get_attribute("currency")

    def get_donation_date(self) -> datetime | None:
        """Get the donation date."""
        donation_date = self.get_attribute("donation_date")
        if donation_date:
            return datetime.fromisoformat(donation_date.replace("Z", "+00:00"))
        return None

    def get_created_at(self) -> datetime | None:
        """Get the donation creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the donation last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_fund_id(self) -> str | None:
        """Get the fund ID."""
        fund_data = self.get_relationship_data("fund")
        if fund_data and isinstance(fund_data, dict):
            return fund_data.get("id")
        return None

    def get_batch_id(self) -> str | None:
        """Get the batch ID."""
        batch_data = self.get_relationship_data("batch")
        if batch_data and isinstance(batch_data, dict):
            return batch_data.get("id")
        return None


class PCOFund(PCOResource):
    """Represents a fund in Planning Center Giving."""

    def get_name(self) -> str | None:
        """Get the fund name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the fund description."""
        return self.get_attribute("description")

    def get_created_at(self) -> datetime | None:
        """Get the fund creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the fund last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCOBatch(PCOResource):
    """Represents a batch in Planning Center Giving."""

    def get_name(self) -> str | None:
        """Get the batch name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the batch description."""
        return self.get_attribute("description")

    def get_created_at(self) -> datetime | None:
        """Get the batch creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the batch last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None


class PCODesignation(PCOResource):
    """Represents a designation in Planning Center Giving."""

    def get_amount(self) -> Decimal | None:
        """Get the designation amount."""
        amount = self.get_attribute("amount")
        if amount is not None:
            return Decimal(str(amount))
        return None

    def get_created_at(self) -> datetime | None:
        """Get the designation creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the designation last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_donation_id(self) -> str | None:
        """Get the donation ID."""
        donation_data = self.get_relationship_data("donation")
        if donation_data and isinstance(donation_data, dict):
            return donation_data.get("id")
        return None

    def get_fund_id(self) -> str | None:
        """Get the fund ID."""
        fund_data = self.get_relationship_data("fund")
        if fund_data and isinstance(fund_data, dict):
            return fund_data.get("id")
        return None


class PCOPledge(PCOResource):
    """Represents a pledge in Planning Center Giving."""

    def get_amount(self) -> Decimal | None:
        """Get the pledge amount."""
        amount = self.get_attribute("amount")
        if amount is not None:
            return Decimal(str(amount))
        return None

    def get_pledge_date(self) -> datetime | None:
        """Get the pledge date."""
        pledge_date = self.get_attribute("pledge_date")
        if pledge_date:
            return datetime.fromisoformat(pledge_date.replace("Z", "+00:00"))
        return None

    def get_created_at(self) -> datetime | None:
        """Get the pledge creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the pledge last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_fund_id(self) -> str | None:
        """Get the fund ID."""
        fund_data = self.get_relationship_data("fund")
        if fund_data and isinstance(fund_data, dict):
            return fund_data.get("id")
        return None


class PCORecurringDonation(PCOResource):
    """Represents a recurring donation in Planning Center Giving."""

    def get_amount(self) -> Decimal | None:
        """Get the recurring donation amount."""
        amount = self.get_attribute("amount")
        if amount is not None:
            return Decimal(str(amount))
        return None

    def get_frequency(self) -> str | None:
        """Get the recurring donation frequency."""
        return self.get_attribute("frequency")

    def get_next_donation_date(self) -> datetime | None:
        """Get the next donation date."""
        next_donation_date = self.get_attribute("next_donation_date")
        if next_donation_date:
            return datetime.fromisoformat(next_donation_date.replace("Z", "+00:00"))
        return None

    def get_created_at(self) -> datetime | None:
        """Get the recurring donation creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the recurring donation last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_fund_id(self) -> str | None:
        """Get the fund ID."""
        fund_data = self.get_relationship_data("fund")
        if fund_data and isinstance(fund_data, dict):
            return fund_data.get("id")
        return None
