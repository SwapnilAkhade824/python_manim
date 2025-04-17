from manim import *

class ExactDerangement(Scene):
    def construct(self):
        # Setup
        card_width, card_height = 0.8, 1.2
        back_color = BLUE_D
        
        # Create cards 1-10 (back side up)
        cards = VGroup(*[
            VGroup(
                Rectangle(width=card_width, height=card_height,
                         fill_color=back_color, fill_opacity=1,
                         stroke_color=WHITE, stroke_width=2),
                Tex(str(i), color=WHITE, font_size=36)
            ) for i in range(1, 11)
        ])
        
        # Stack cards at bottom center
        deck = cards.copy()
        deck.arrange(DOWN, buff=-1.0).shift(DOWN*2.5)
        for card in deck:
            card[1].set_opacity(0)  # Hide numbers initially
            
        # Create position markers 1-10 at top
        positions = VGroup(*[
            VGroup(
                Rectangle(width=card_width, height=card_height,
                        stroke_color=WHITE, stroke_width=1),
                Tex(str(i), color=WHITE, font_size=30)
            ).arrange(RIGHT, buff=0.5).shift(UP*2.5 + LEFT*4.5)
            for i in range(1, 11)
        ])
        
        # Show initial setup
        self.play(FadeIn(deck), FadeIn(positions))
        self.wait(0.5)
        
        # Your exact derangement mapping
        derangement = {
            0: 8,   # Position 1 gets card 8
            1: 7,   # Position 2 gets card 7
            2: 10,  # Position 3 gets card 10
            3: 9,   # Position 4 gets card 9
            4: 6,   # Position 5 gets card 6
            5: 1,   # Position 6 gets card 1
            6: 3,   # Position 7 gets card 3
            7: 2,   # Position 8 gets card 2
            8: 5,   # Position 9 gets card 5
            9: 4    # Position 10 gets card 4
        }
        
        # Deal cards according to derangement
        for pos_idx in range(10):
            # Find the card we need (cards are 0-9 in list but numbered 1-10)
            card_num = derangement[pos_idx]
            card = [c for c in deck if int(c[1].tex_string) == card_num][0]
            
            # Flip animation
            self.play(
                card[0].animate.rotate(PI/2, about_edge=UP).set_fill(opacity=0),
                card[1].animate.set_opacity(1),
                run_time=0.5
            )
            
            # Move to position
            target_pos = positions[pos_idx].get_center()
            self.play(
                card.animate.move_to(target_pos),
                run_time=1
            )
            
            # Verify no match (position number is pos_idx+1)
            if int(card[1].tex_string) == pos_idx+1:
                self.play(Flash(card, color=RED))
            
            # Remove from deck
            deck.remove(card)
            self.wait(0.3)
        
        # Confirm derangement
        text = Tex("Complete Derangement (no matches)", color=GREEN)
        self.play(Write(text))
        self.play(Flash(text))
        self.wait(2)