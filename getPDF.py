from reportlab.pdfgen import canvas
from hashlib import sha256
from getKeyWords import sample_analyze_entities
from fill_blanks import get_blank_questions
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.platypus import (Flowable, Paragraph, SimpleDocTemplate, Spacer)
import os


def getHash(text):
    m = sha256()
    m.update(str.encode(text))
    return m.hexdigest()


def drawText(x, y, c, text):
    textobject = c.beginText()
    textobject.setTextOrigin(x, y)
    textobject.setFont('Times-Roman', 14)
    textobject.textLine(text)
    c.drawText(textobject)


class BoxText(Flowable):

    # ----------------------------------------------------------------------
    def __init__(self, x=0 * inch, y=0 * inch, width=3.68 * inch, height=2.45 * inch, text1="", text2=""):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text1 = text1
        self.text2 = text2
        self.styles = getSampleStyleSheet()

    # ----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        """
        http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height - y * unit
        return x, y

    # ----------------------------------------------------------------------
    def draw(self):
        """
        Draw the shape, text, etc
        """
        self.canv.rect(self.x, self.y, self.width, self.height)
        self.canv.rect(self.x + self.width, self.y, self.width, self.height)
        p1 = Paragraph(self.text1, style=self.styles["Normal"])
        p1.wrapOn(self.canv, self.width - 10, self.height)
        p1.drawOn(self.canv, *self.coord(self.x + 0.1, self.y + 2.40, inch))
        p2 = Paragraph(self.text2, style=self.styles["Normal"])
        p2.wrapOn(self.x + self.width, self.width - 10, self.height)
        p2.drawOn(self.canv, *self.coord(self.x + 3.68 + 0.1, self.y + 2.40, inch))


def getString(answers):
    string = ""
    for answer in answers[1]:
        string += "[" + str(answer[0]) + "] " + answer[1] + '\n'
    return string


def getPDF(text, keywords):
    questionAnswers = get_blank_questions(text, keywords)
    filename = "card_" + getHash(text) + ".pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=0.5 * inch,
                            leftMargin=0.5 * inch, topMargin=0.5 * inch, bottomMargin=0.5 * inch)
    story = []
    i = 0
    while i < len(questionAnswers):
        # draw questions
        j = 0
        while j < 8 and i + j < len(questionAnswers):
            if j + 1 < len(questionAnswers):
                box = BoxText(text1=questionAnswers[j][0], text2=questionAnswers[j + 1][0])
                story.append(box)
                j += 2
            else:
                if j + 1 == len(questionAnswers):
                    box = BoxText(text1=questionAnswers[j][0])
                    story.append(box)
                    j += 2
        while j < 8:
            # Add boxes until fill up page.
            story.append(BoxText())
            j += 2
        # drawAnswers
        j = 0
        while j < 8 and i + j < len(questionAnswers):
            if j + 1 < len(questionAnswers):
                box = BoxText(text1=getString(questionAnswers[j + 1]), text2=getString(questionAnswers[j]))

            else:
                box = BoxText(text2=getString(questionAnswers[j]))
            story.append(box)
            j += 2
        i += 8

    doc.build(story)
    return filename


if __name__ == "__main__":
    getPDF()
