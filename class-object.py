class person:
    def __init__(self, fname, lname, bod, occupation):
        self.fname = fname
        self.lname = lname
        self.bod = bod
        self.occupation = occupation

    def intro(self):
        return(f"hi i am {self.fname}")

p1 = person("hari", "shresth", "2000-9-1", "jobless")
print(p1.intro())