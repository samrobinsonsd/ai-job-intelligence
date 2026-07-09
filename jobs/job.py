class Job:

    def __init__(
        self,
        title,
        company,
        location,
        salary=0,
        source="Unknown",
        url="",
        description="",
        labels=None
    ):
        self.title = title
        self.company = company
        self.location = location
        self.salary = salary
        self.source = source
        self.url = url
        self.description = description
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
            source=data.get("source", "Unknown"),
            url=data.get("url", ""),
            description=data.get("description", ""),
            labels=data.get("labels", [])
        )

    def __str__(self):
        return (
            f"{self.title} | "
            f"{self.company} | "
            f"{self.location} | "
            f"${self.salary}"
        )

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "salary": self.salary,
            "source": self.source,
            "url": self.url,
            "description": self.description,
            "labels": self.labels,
            "score": self.score,
            "decision": self.decision,
            "reasons": self.reasons,
            "summary": self.summary,
        }