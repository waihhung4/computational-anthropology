from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


tokenizer = AutoTokenizer.from_pretrained("mdarhri00/named-entity-recognition")
model = AutoModelForTokenClassification.from_pretrained("mdarhri00/named-entity-recognition")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)

example = """The story of Noah's flood is primarily derived from the biblical narrative found in the Book of Genesis, and while many ancient cultures have their own flood myths, the absence of a direct account of Noah's flood in the records of the early civilizations you mentioned can be attributed to several factors:
Cultural Context: The flood narrative in the Bible is specific to the Hebrew tradition. Other civilizations had their own mythologies, which did include flood stories (e.g., the Epic of Gilgamesh in Mesopotamia). These narratives often reflect the culture, values, and historical experiences of the societies that produced them, rather than being universal accounts.
Geographical Differences: The civilizations you mentioned were located in different regions with distinct environmental and geological contexts. Flooding events may not have been significant or catastrophic in their areas to warrant a lasting narrative like that of Noah’s flood. For example, the Nile River's predictable flooding was essential to Egyptian agriculture and may have been viewed positively rather than as a destructive force.
Historical Documentation: The record-keeping practices varied significantly among these civilizations. While the Sumerians and Egyptians had advanced writing systems, their records often focused on political, economic, and religious matters rather than mythological events. The absence of a record does not necessarily imply that such an event did not occur; it may simply reflect what was deemed significant enough to document.
Mythological Syncretism: Flood myths are common across various cultures, but the details and interpretations can differ greatly. For instance, the Mesopotamian flood myth in the Epic of Gilgamesh shares some similarities with the Noah story but is distinct in its details and implications. These variations suggest that while flood events might have been widespread, their interpretations and the resulting narratives were shaped by each culture’s unique worldview.
Timing and Archaeological Evidence: The timeline of these civilizations and their development varies. The earliest texts from these cultures may not correspond chronologically with the biblical story, and archaeological evidence of a massive flood in the regions inhabited by these civilizations has not been definitively linked to a single event like Noah’s flood.
In summary, the absence of Noah's flood in the records of these early civilizations reflects a combination of cultural, geographical, and historical factors rather than a lack of significant flood events in their histories. Each civilization developed its own narratives based on their experiences and environments, leading to diverse mythologies that may share themes but do not replicate each other’s stories."""

ner_results = nlp(example)

for ner in ner_results:
    print(ner["word"] + " : " + ner["entity"])