class Job:

    def __init__(
        self,
        title,
        company,
        location,
        salary=0,
        compensation_min=0,
        compensation_max=0,
        compensation_type="",
        source="Unknown",
        url="",
        labels=None
    ):
        self.title = title
        self.company = company
        self.location = location
        self.salary = salary
        self.compensation_min = compensation_min
        self.compensation_max = compensation_max
        self.compensation_type = compensation_type
        self.source = source
        self.url = url
        self.labels = labels or []
        self.message_id = ""
        self.score = 0
        self.decision = None
        self.reasons = []
        self.summary = ""

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Job object from a dictionary.

        Parameters:
            data (dict): Dictionary containing job information.

        Returns:
            Job
        """

        return cls(
            title=data["title"],
            company=data["company"],
            location=data["location"],
            salary=data.get("salary", 0),
            compensation_min=data.get("compensation_min", 0),
            compensation_max=data.get("compensation_max", 0),
            compensation_type=data.get("compensation_type", ""),
            source=data.get("source", "Unknown"),
            url=data.get("url", ""),
            labels=data.get("labels", []),
    )

    def __str__(self):
        return f"{self.title} | {self.company} | {self.location} | ${self.salary}"

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "salary": self.salary,
            "compensation_min": self.compensation_min,
            "compensation_max": self.compensation_max,
            "compensation_type": self.compensation_type,
            "source": self.source,
            "url": self.url,
            "labels": self.labels,
            "score": self.score,
            "decision": self.decision,
            "reasons": self.reasons,
            "summary": self.summary,
        }