class Card:
    def __init__(self, title, subtitle, image_url, description):
        self.title = title
        self.subtitle = subtitle
        self.image_url = image_url
        self.description = description

    def render(self):
        return f"""
        <div class="card">
            <img src="{self.image_url}" alt="{self.title}">
            <h2>{self.title}</h2>
            <p>{self.subtitle}</p>
            <p>{self.description}</p>
        </div>
        """

class CardComponent:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def render(self):
        html = ""
        for card in self.cards:
            html += card.render()
        return html

# Misol foydalanish:
card1 = Card("Card 1", "Subtitle 1", "https://example.com/image1.jpg", "Description 1")
card2 = Card("Card 2", "Subtitle 2", "https://example.com/image2.jpg", "Description 2")

component = CardComponent()
component.add_card(card1)
component.add_card(card2)

print(component.render())
