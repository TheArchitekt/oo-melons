"""Classes for melon orders."""


class DomesticMelonOrder:
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder:
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    order_type = None

    tax = 0

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas melon":
            base_price*= 1.5
        total = (1 + self.tax) * self.qty * base_price
        if self.qty < 10 and self.order_type == "international":
            total += 3



        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    order_type = 'international'
    tax = 0.17
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)

        self.country_code = country_code

    def get_country_code(self):

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    order_type = 'domestic'
    tax = 0.08


class GovernmentMelonOrder(AbstractMelonOrder):
    order_type = 'government'
    tax = 0

    def __init__(self, species, qty, passed_inspection):
        super().__init__(species, qty)

        self.passed_inspection = False

    def inspection_status(self, passed):

        self.passed_inspection = passed
