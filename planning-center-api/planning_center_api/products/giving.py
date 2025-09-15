"""Giving product models for Planning Center API."""

from datetime import datetime

from ..models.base import PCOResource


class PCOBatch(PCOResource):
    """Represents a batch in Planning Center Giving."""

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

    def get_committed_at(self) -> datetime | None:
        """Get the batch commit time."""
        committed_at = self.get_attribute("committed_at")
        if committed_at:
            return datetime.fromisoformat(committed_at.replace("Z", "+00:00"))
        return None

    def get_description(self) -> str | None:
        """Get the batch description."""
        return self.get_attribute("description")

    def get_donations_count(self) -> int | None:
        """Get the number of donations in the batch."""
        return self.get_attribute("donations_count")

    def get_total_cents(self) -> int | None:
        """Get the total amount in cents."""
        return self.get_attribute("total_cents")

    def get_total_currency(self) -> str | None:
        """Get the currency of the total amount."""
        return self.get_attribute("total_currency")

    def get_status(self) -> str | None:
        """Get the batch status (in_progress, updating, or committed)."""
        return self.get_attribute("status")

    def get_batch_group_id(self) -> str | None:
        """Get the batch group ID."""
        batch_group_data = self.get_relationship_data("batch_group")
        if batch_group_data and isinstance(batch_group_data, dict):
            return batch_group_data.get("id")
        return None


class PCOBatchGroup(PCOResource):
    """Represents a batch group in Planning Center Giving."""

    def get_created_at(self) -> datetime | None:
        """Get the batch group creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the batch group last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_description(self) -> str | None:
        """Get the batch group description."""
        return self.get_attribute("description")

    def get_committed(self) -> bool | None:
        """Get whether the batch group is committed."""
        return self.get_attribute("committed")

    def get_total_cents(self) -> int | None:
        """Get the total amount in cents."""
        return self.get_attribute("total_cents")

    def get_total_currency(self) -> str | None:
        """Get the currency of the total amount."""
        return self.get_attribute("total_currency")

    def get_status(self) -> str | None:
        """Get the batch group status (in_progress, updating, or committed)."""
        return self.get_attribute("status")


class PCOCampus(PCOResource):
    """Represents a campus in Planning Center Giving."""

    def get_name(self) -> str | None:
        """Get the campus name."""
        return self.get_attribute("name")

    def get_address(self) -> dict | None:
        """Get the campus address."""
        return self.get_attribute("address")


class PCODesignation(PCOResource):
    """Represents a designation in Planning Center Giving."""

    def get_amount_cents(self) -> int | None:
        """Get the designation amount in cents."""
        return self.get_attribute("amount_cents")

    def get_amount_currency(self) -> str | None:
        """Get the currency of the amount."""
        return self.get_attribute("amount_currency")

    def get_fee_cents(self) -> int | None:
        """Get the fee amount in cents."""
        return self.get_attribute("fee_cents")

    def get_fund_id(self) -> str | None:
        """Get the fund ID."""
        fund_data = self.get_relationship_data("fund")
        if fund_data and isinstance(fund_data, dict):
            return fund_data.get("id")
        return None


class PCODesignationRefund(PCOResource):
    """Represents a designation refund in Planning Center Giving."""

    def get_amount_cents(self) -> int | None:
        """Get the refund amount in cents."""
        return self.get_attribute("amount_cents")

    def get_amount_currency(self) -> str | None:
        """Get the currency of the amount."""
        return self.get_attribute("amount_currency")

    def get_designation_id(self) -> str | None:
        """Get the designation ID."""
        designation_data = self.get_relationship_data("designation")
        if designation_data and isinstance(designation_data, dict):
            return designation_data.get("id")
        return None


class PCODonation(PCOResource):
    """Represents a donation in Planning Center Giving."""

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

    def get_payment_method_sub(self) -> str | None:
        """Get the payment method subtype (credit, debit, prepaid, or unknown)."""
        return self.get_attribute("payment_method_sub")

    def get_payment_last4(self) -> str | None:
        """Get the last 4 digits of the payment method."""
        return self.get_attribute("payment_last4")

    def get_payment_brand(self) -> str | None:
        """Get the payment brand (Visa, Mastercard, etc.)."""
        return self.get_attribute("payment_brand")

    def get_payment_check_number(self) -> int | None:
        """Get the check number for check donations."""
        return self.get_attribute("payment_check_number")

    def get_payment_check_dated_at(self) -> datetime | None:
        """Get the check date for check donations."""
        check_date = self.get_attribute("payment_check_dated_at")
        if check_date:
            return datetime.fromisoformat(check_date.replace("Z", "+00:00"))
        return None

    def get_fee_cents(self) -> int | None:
        """Get the processing fee in cents."""
        return self.get_attribute("fee_cents")

    def get_payment_method(self) -> str | None:
        """Get the payment method (ach, cash, check, or card)."""
        return self.get_attribute("payment_method")

    def get_received_at(self) -> datetime | None:
        """Get when the donation was received."""
        received_at = self.get_attribute("received_at")
        if received_at:
            return datetime.fromisoformat(received_at.replace("Z", "+00:00"))
        return None

    def get_amount_cents(self) -> int | None:
        """Get the donation amount in cents."""
        return self.get_attribute("amount_cents")

    def get_payment_status(self) -> str | None:
        """Get the payment status (pending, succeeded, or failed)."""
        return self.get_attribute("payment_status")

    def get_completed_at(self) -> datetime | None:
        """Get when the donation was completed."""
        completed_at = self.get_attribute("completed_at")
        if completed_at:
            return datetime.fromisoformat(completed_at.replace("Z", "+00:00"))
        return None

    def get_fee_covered(self) -> bool | None:
        """Get whether the donor covered the processing fee."""
        return self.get_attribute("fee_covered")

    def get_amount_currency(self) -> str | None:
        """Get the currency of the amount."""
        return self.get_attribute("amount_currency")

    def get_fee_currency(self) -> str | None:
        """Get the currency of the fee."""
        return self.get_attribute("fee_currency")

    def get_refunded(self) -> bool | None:
        """Get whether the donation has been refunded."""
        return self.get_attribute("refunded")

    def get_refundable(self) -> bool | None:
        """Get whether the donation can be refunded."""
        return self.get_attribute("refundable")

    def get_batch_id(self) -> str | None:
        """Get the batch ID."""
        batch_data = self.get_relationship_data("batch")
        if batch_data and isinstance(batch_data, dict):
            return batch_data.get("id")
        return None

    def get_campus_id(self) -> str | None:
        """Get the campus ID."""
        campus_data = self.get_relationship_data("campus")
        if campus_data and isinstance(campus_data, dict):
            return campus_data.get("id")
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_payment_source_id(self) -> str | None:
        """Get the payment source ID."""
        payment_source_data = self.get_relationship_data("payment_source")
        if payment_source_data and isinstance(payment_source_data, dict):
            return payment_source_data.get("id")
        return None

    def get_recurring_donation_id(self) -> str | None:
        """Get the recurring donation ID."""
        recurring_donation_data = self.get_relationship_data("recurring_donation")
        if recurring_donation_data and isinstance(recurring_donation_data, dict):
            return recurring_donation_data.get("id")
        return None


class PCOFund(PCOResource):
    """Represents a fund in Planning Center Giving."""

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

    def get_name(self) -> str | None:
        """Get the fund name."""
        return self.get_attribute("name")

    def get_ledger_code(self) -> str | None:
        """Get the fund ledger code."""
        return self.get_attribute("ledger_code")

    def get_description(self) -> str | None:
        """Get the fund description."""
        return self.get_attribute("description")

    def get_visibility(self) -> str | None:
        """Get the fund visibility (everywhere, admin_only, nowhere, or hidden)."""
        return self.get_attribute("visibility")

    def get_default(self) -> bool | None:
        """Get whether this is the default fund."""
        return self.get_attribute("default")

    def get_color(self) -> str | None:
        """Get the fund color."""
        return self.get_attribute("color")

    def get_deletable(self) -> bool | None:
        """Get whether the fund can be deleted."""
        return self.get_attribute("deletable")

    def get_slug(self) -> str | None:
        """Get the fund slug."""
        return self.get_attribute("slug")


class PCOInKindDonation(PCOResource):
    """Represents an in-kind donation in Planning Center Giving."""

    def get_created_at(self) -> datetime | None:
        """Get the in-kind donation creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the in-kind donation last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_description(self) -> str | None:
        """Get the in-kind donation description."""
        return self.get_attribute("description")

    def get_exchange_details(self) -> str | None:
        """Get the exchange details."""
        return self.get_attribute("exchange_details")

    def get_fair_market_value_cents(self) -> int | None:
        """Get the fair market value in cents."""
        return self.get_attribute("fair_market_value_cents")

    def get_received_on(self) -> datetime | None:
        """Get the date the in-kind donation was received."""
        received_on = self.get_attribute("received_on")
        if received_on:
            return datetime.fromisoformat(received_on.replace("Z", "+00:00"))
        return None

    def get_valuation_details(self) -> str | None:
        """Get the valuation details."""
        return self.get_attribute("valuation_details")

    def get_acknowledgment_last_sent_at(self) -> datetime | None:
        """Get when the acknowledgment was last sent."""
        acknowledgment_date = self.get_attribute("acknowledgment_last_sent_at")
        if acknowledgment_date:
            return datetime.fromisoformat(acknowledgment_date.replace("Z", "+00:00"))
        return None

    def get_fair_market_value_currency(self) -> str | None:
        """Get the currency of the fair market value."""
        return self.get_attribute("fair_market_value_currency")

    def get_fund_id(self) -> str | None:
        """Get the fund ID."""
        fund_data = self.get_relationship_data("fund")
        if fund_data and isinstance(fund_data, dict):
            return fund_data.get("id")
        return None

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_campus_id(self) -> str | None:
        """Get the campus ID."""
        campus_data = self.get_relationship_data("campus")
        if campus_data and isinstance(campus_data, dict):
            return campus_data.get("id")
        return None


class PCOLabel(PCOResource):
    """Represents a label in Planning Center Giving."""

    def get_slug(self) -> str | None:
        """Get the label slug."""
        return self.get_attribute("slug")


class PCONote(PCOResource):
    """Represents a note in Planning Center Giving."""

    def get_body(self) -> str | None:
        """Get the note body."""
        return self.get_attribute("body")


class PCOGivingOrganization(PCOResource):
    """Represents an organization in Planning Center Giving."""

    def get_name(self) -> str | None:
        """Get the organization name."""
        return self.get_attribute("name")

    def get_time_zone(self) -> str | None:
        """Get the organization time zone."""
        return self.get_attribute("time_zone")

    def get_text2give_enabled(self) -> bool | None:
        """Get whether text-to-give is enabled."""
        return self.get_attribute("text2give_enabled")


class PCOPaymentMethod(PCOResource):
    """Represents a payment method in Planning Center Giving."""

    def get_created_at(self) -> datetime | None:
        """Get the payment method creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the payment method last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_method_type(self) -> str | None:
        """Get the payment method type (card, us_bank_account, or au_becs_debit)."""
        return self.get_attribute("method_type")

    def get_method_subtype(self) -> str | None:
        """Get the payment method subtype."""
        return self.get_attribute("method_subtype")

    def get_last4(self) -> str | None:
        """Get the last 4 digits of the payment method."""
        return self.get_attribute("last4")

    def get_brand(self) -> str | None:
        """Get the payment method brand."""
        return self.get_attribute("brand")

    def get_expiration(self) -> datetime | None:
        """Get the payment method expiration date."""
        expiration = self.get_attribute("expiration")
        if expiration:
            return datetime.fromisoformat(expiration.replace("Z", "+00:00"))
        return None

    def get_verified(self) -> bool | None:
        """Get whether the payment method is verified."""
        return self.get_attribute("verified")


class PCOPaymentSource(PCOResource):
    """Represents a payment source in Planning Center Giving."""

    def get_created_at(self) -> datetime | None:
        """Get the payment source creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the payment source last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_name(self) -> str | None:
        """Get the payment source name."""
        return self.get_attribute("name")


class PCOGivingPerson(PCOResource):
    """Represents a person in Planning Center Giving."""

    def get_permissions(self) -> str | None:
        """Get the person's permissions (administrator, reviewer, counter, or bookkeeper)."""
        return self.get_attribute("permissions")

    def get_email_addresses(self) -> list[dict] | None:
        """Get the person's email addresses."""
        return self.get_attribute("email_addresses")

    def get_addresses(self) -> list[dict] | None:
        """Get the person's addresses."""
        return self.get_attribute("addresses")

    def get_phone_numbers(self) -> list[dict] | None:
        """Get the person's phone numbers."""
        return self.get_attribute("phone_numbers")

    def get_first_name(self) -> str | None:
        """Get the person's first name."""
        return self.get_attribute("first_name")

    def get_last_name(self) -> str | None:
        """Get the person's last name."""
        return self.get_attribute("last_name")

    def get_donor_number(self) -> int | None:
        """Get the person's donor number."""
        return self.get_attribute("donor_number")

    def get_first_donated_at(self) -> datetime | None:
        """Get when the person first donated."""
        first_donated_at = self.get_attribute("first_donated_at")
        if first_donated_at:
            return datetime.fromisoformat(first_donated_at.replace("Z", "+00:00"))
        return None

    def get_primary_campus_id(self) -> str | None:
        """Get the primary campus ID."""
        primary_campus_data = self.get_relationship_data("primary_campus")
        if primary_campus_data and isinstance(primary_campus_data, dict):
            return primary_campus_data.get("id")
        return None


class PCOPledge(PCOResource):
    """Represents a pledge in Planning Center Giving."""

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

    def get_amount_cents(self) -> int | None:
        """Get the pledge amount in cents."""
        return self.get_attribute("amount_cents")

    def get_amount_currency(self) -> str | None:
        """Get the currency of the amount."""
        return self.get_attribute("amount_currency")

    def get_joint_giver_amount_cents(self) -> int | None:
        """Get the joint giver amount in cents."""
        return self.get_attribute("joint_giver_amount_cents")

    def get_donated_total_cents(self) -> int | None:
        """Get the total donated amount in cents."""
        return self.get_attribute("donated_total_cents")

    def get_joint_giver_donated_total_cents(self) -> int | None:
        """Get the joint giver total donated amount in cents."""
        return self.get_attribute("joint_giver_donated_total_cents")

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None

    def get_pledge_campaign_id(self) -> str | None:
        """Get the pledge campaign ID."""
        pledge_campaign_data = self.get_relationship_data("pledge_campaign")
        if pledge_campaign_data and isinstance(pledge_campaign_data, dict):
            return pledge_campaign_data.get("id")
        return None


class PCOPledgeCampaign(PCOResource):
    """Represents a pledge campaign in Planning Center Giving."""

    def get_created_at(self) -> datetime | None:
        """Get the pledge campaign creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the pledge campaign last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_name(self) -> str | None:
        """Get the pledge campaign name."""
        return self.get_attribute("name")

    def get_description(self) -> str | None:
        """Get the pledge campaign description."""
        return self.get_attribute("description")

    def get_starts_at(self) -> datetime | None:
        """Get when the pledge campaign starts."""
        starts_at = self.get_attribute("starts_at")
        if starts_at:
            return datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        return None

    def get_ends_at(self) -> datetime | None:
        """Get when the pledge campaign ends."""
        ends_at = self.get_attribute("ends_at")
        if ends_at:
            return datetime.fromisoformat(ends_at.replace("Z", "+00:00"))
        return None

    def get_goal_cents(self) -> int | None:
        """Get the pledge campaign goal in cents."""
        return self.get_attribute("goal_cents")

    def get_goal_currency(self) -> str | None:
        """Get the currency of the goal."""
        return self.get_attribute("goal_currency")

    def get_show_goal_in_church_center(self) -> bool | None:
        """Get whether to show the goal in Church Center."""
        return self.get_attribute("show_goal_in_church_center")

    def get_received_total_from_pledges_cents(self) -> int | None:
        """Get the total received from pledges in cents."""
        return self.get_attribute("received_total_from_pledges_cents")

    def get_received_total_outside_of_pledges_cents(self) -> int | None:
        """Get the total received outside of pledges in cents."""
        return self.get_attribute("received_total_outside_of_pledges_cents")

    def get_fund_id(self) -> str | None:
        """Get the fund ID."""
        fund_data = self.get_relationship_data("fund")
        if fund_data and isinstance(fund_data, dict):
            return fund_data.get("id")
        return None


class PCORecurringDonation(PCOResource):
    """Represents a recurring donation in Planning Center Giving."""

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

    def get_release_hold_at(self) -> datetime | None:
        """Get when the hold will be released."""
        release_hold_at = self.get_attribute("release_hold_at")
        if release_hold_at:
            return datetime.fromisoformat(release_hold_at.replace("Z", "+00:00"))
        return None

    def get_amount_cents(self) -> int | None:
        """Get the recurring donation amount in cents."""
        return self.get_attribute("amount_cents")

    def get_status(self) -> str | None:
        """Get the recurring donation status (active, indefinite_hold, or temporary_hold)."""
        return self.get_attribute("status")

    def get_last_donation_received_at(self) -> datetime | None:
        """Get when the last donation was received."""
        last_donation_date = self.get_attribute("last_donation_received_at")
        if last_donation_date:
            return datetime.fromisoformat(last_donation_date.replace("Z", "+00:00"))
        return None

    def get_next_occurrence(self) -> datetime | None:
        """Get the next donation occurrence."""
        next_occurrence = self.get_attribute("next_occurrence")
        if next_occurrence:
            return datetime.fromisoformat(next_occurrence.replace("Z", "+00:00"))
        return None

    def get_schedule(self) -> dict | None:
        """Get the donation schedule."""
        return self.get_attribute("schedule")

    def get_amount_currency(self) -> str | None:
        """Get the currency of the amount."""
        return self.get_attribute("amount_currency")

    def get_person_id(self) -> str | None:
        """Get the person ID."""
        person_data = self.get_relationship_data("person")
        if person_data and isinstance(person_data, dict):
            return person_data.get("id")
        return None


class PCORecurringDonationDesignation(PCOResource):
    """Represents a recurring donation designation in Planning Center Giving."""

    def get_amount_cents(self) -> int | None:
        """Get the designation amount in cents."""
        return self.get_attribute("amount_cents")

    def get_amount_currency(self) -> str | None:
        """Get the currency of the amount."""
        return self.get_attribute("amount_currency")

    def get_fund_id(self) -> str | None:
        """Get the fund ID."""
        fund_data = self.get_relationship_data("fund")
        if fund_data and isinstance(fund_data, dict):
            return fund_data.get("id")
        return None


class PCORefund(PCOResource):
    """Represents a refund in Planning Center Giving."""

    def get_created_at(self) -> datetime | None:
        """Get the refund creation time."""
        created_at = self.get_attribute("created_at")
        if created_at:
            return datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return None

    def get_updated_at(self) -> datetime | None:
        """Get the refund last update time."""
        updated_at = self.get_attribute("updated_at")
        if updated_at:
            return datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        return None

    def get_amount_cents(self) -> int | None:
        """Get the refund amount in cents."""
        return self.get_attribute("amount_cents")

    def get_amount_currency(self) -> str | None:
        """Get the currency of the amount."""
        return self.get_attribute("amount_currency")

    def get_fee_cents(self) -> int | None:
        """Get the refund fee in cents."""
        return self.get_attribute("fee_cents")

    def get_refunded_at(self) -> datetime | None:
        """Get when the refund was processed."""
        refunded_at = self.get_attribute("refunded_at")
        if refunded_at:
            return datetime.fromisoformat(refunded_at.replace("Z", "+00:00"))
        return None

    def get_fee_currency(self) -> str | None:
        """Get the currency of the fee."""
        return self.get_attribute("fee_currency")
