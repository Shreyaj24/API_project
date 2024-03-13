class TerminatedPostcode:

    def __init__(self, postcode, year_terminated, month_terminated):
        self.postcode = postcode
        self.year_terminated = year_terminated
        self.month_terminated = month_terminated

    def setYearTerminated(self, year_terminated):
        self.year_terminated = year_terminated

    def setMonthTerminated(selfself, month_terminated):
        self.month_terminated = month_terminated

    def __repr__(self):
        terminated_postcode_data = f"postcode: {self.postcode}, year_terminated: {self.year_terminated}, month_terminated= {self.month_terminated}"
        return terminated_postcode_data
