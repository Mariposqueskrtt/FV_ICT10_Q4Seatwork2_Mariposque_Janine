from js import document


class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.subject}."


classmates = [
    Classmate("Alexandra Vargas", "Emerald", "Social Studies"),
    Classmate("Xylee Goyenechea", "Emerald", "Science"),
    Classmate("KC Del Prado", "Emerald", "Social Studies"),
    Classmate("Rycob Pagtalunan", "Emerald", "Math"),
    Classmate("Miguel Buo", "Emerald", "English")
]


def get(id):
    return document.getElementById(id).value


def clear_inputs():
    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""


#shows the list of classmates, along with new classmates added
def show_list(event=None):
    output = "<h3>Classmates:</h3>"

    for c in classmates:
        output += f"<p>{c.introduce()}</p>"

    document.getElementById("list").innerHTML = output


# adding classmates to the lists
def add_classmate(event=None):
    name = get("name")
    section = get("section")
    subject = get("subject")

    if not name or not section or not subject:
        document.getElementById("list").innerHTML = "Kindly please answer all the questions"
        return

    classmates.append(Classmate(name, section, subject))

    clear_inputs()

    #shows confirmation of being added successfully, but does not show the list of classmates
    document.getElementById("list").innerHTML = "You have been added successfully!"