//
//  CardGameViewController.m
//  Matchismo
//
//  Created by liszt on 6/17/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import "CardGameViewController.h"
#import "GameScoreViewController.h"

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
@property (weak, nonatomic) IBOutlet UISwitch *modSwitchBtn;
@property (weak, nonatomic) IBOutlet UILabel *matchInfo;
@property (strong, nonatomic) NSMutableArray *score_his;

@end

@implementation CardGameViewController

- (void) prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    if ([segue.identifier isEqualToString:@"showHisScore"])
    {
        if ([segue.destinationViewController isKindOfClass:[GameScoreViewController class]])
        {
            GameScoreViewController *gsvc = (GameScoreViewController *)segue.destinationViewController;
            gsvc.score_his = self.score_his;
        }
    }
}

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

- (NSMutableArray *) score_his
{
    if (! _score_his)
    {
        _score_his = [[NSMutableArray alloc] init];
    }
    
    return _score_his;
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
    NSUInteger choosenButtonIndex = [self.cardButtons
                                     indexOfObject:sender];
    [self.game chooseCardAtIndex:choosenButtonIndex];
    [self updateUI];
    self.flipCount = self.flipCount + 1;
    self.scoreLabel.text = [NSString stringWithFormat:@"Score: %ld",
                            self.game.score];
    // task 5
    self.matchInfo.text = self.game.match_info ? self.game.match_info : @"";
    // task 4
    self.modSwitchBtn.enabled = NO;
}
- (IBAction)touchRstBtn:(UIButton *)sender {
    [self.score_his addObject:[NSString stringWithFormat:@"score: %ld",
                               self.game.score]];
    
    self.deck = Nil;
    self.game = Nil;
    self.scoreLabel.text = @"Score: 0";
    [self updateUI];
    
    // task 4
    self.modSwitchBtn.enabled = YES;
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
        NSUInteger cardButtonInedx = [self.cardButtons
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
