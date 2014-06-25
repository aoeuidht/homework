//
//  CardGameViewController.m
//  Matchismo
//
//  Created by liszt on 6/17/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import "CardGameViewController.h"
#import "model/PlayingCardDeck.h"

#import "model/CardMatchingGame.h"

@interface CardGameViewController ()
@property (weak, nonatomic) IBOutlet UILabel *flipsLabel;
@property (nonatomic) int flipCount;
@property (nonatomic) int play_mode;

@property (strong, nonatomic) Deck *deck;
@property (strong, nonatomic) CardMatchingGame *game;
@property (strong, nonatomic) IBOutletCollection(UIButton) NSArray *cardButtons;
@property (weak, nonatomic) IBOutlet UILabel *scoreLabel;

@end

@implementation CardGameViewController

- (int) play_mode
{
    if (_play_mode == 0)
    {
        _play_mode = 2;
    }
    return _play_mode;
}

- (CardMatchingGame *) game
{
    if (! _game)
    {
        _game = [[CardMatchingGame alloc]
                 initWithCardCount:[self.cardButtons count]
                 usingDeck:[self createDeck]
                 atMode: self.play_mode];
    }
    return _game;
}

- (Deck *)deck
{
    if (! _deck) {
        _deck = [self createDeck];
    }
    
    return _deck;
}

- (Deck *)createDeck
{
    return [[PlayingCardDeck alloc] init];
}

- (void)setFlipCount:(int)flipCount
{
    _flipCount = flipCount;
    self.flipsLabel.text = [NSString stringWithFormat:@"Flips: %d", self.flipCount];
}

- (IBAction)touchCardButton:(UIButton *)sender
{
    int choosenButtonIndex = [self.cardButtons
                              indexOfObject:sender];
    [self.game chooseCardAtIndex:choosenButtonIndex];
    [self updateUI];
    self.flipCount = self.flipCount + 1;
    self.scoreLabel.text = [NSString stringWithFormat:@"Score: %d",
                            self.game.score];
}
- (IBAction)touchRstBtn:(UIButton *)sender {
    self.deck = Nil;
    self.game = Nil;
    self.scoreLabel.text = @"Score: 0";
    [self updateUI];
}

- (IBAction)cardModeChange:(UISwitch *)sender {
    int game_mode = sender.isOn ? 3 : 2;
    self.play_mode = game_mode;
    [self touchRstBtn:Nil];
}

- (void) updateUI
{
    for (UIButton *cardButton in self.cardButtons)
    {
        int cardButtonInedx = [self.cardButtons
                               indexOfObject:cardButton];
        Card *card = [self.game cardAtIndex:cardButtonInedx];
        [cardButton setTitle:[self titleForCard:card] forState:UIControlStateNormal];
        [cardButton
         setBackgroundImage:[self backgroundImageForCard:card]
         forState:UIControlStateNormal];
        cardButton.enabled =  ! card.isMatched;
    }
}

- (NSString *) titleForCard:(Card *)card
{
    return card.isChosen ? card.contents : @"";
}

- (UIImage *) backgroundImageForCard:(Card *) card
{
    return [UIImage imageNamed: card.isChosen ?
            @"cardfront" : @"cardback"];
}

@end
