//
//  CardGameViewController.m
//  Matchismo
//
//  Created by liszt on 6/17/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import "CardGameViewController.h"
#import "model/PlayingCardDeck.h"

@interface CardGameViewController ()
@property (weak, nonatomic) IBOutlet UILabel *flipsLabel;
@property (nonatomic) int flipCount;

@property (strong, nonatomic) PlayingCardDeck *deck;
@end

@implementation CardGameViewController

- (Deck *)deck
{
    if (! _deck) {
        _deck = [[PlayingCardDeck alloc] init];
    }
    
    return _deck;
}

- (void)setFlipCount:(int)flipCount
{
    _flipCount = flipCount;
    self.flipsLabel.text = [NSString stringWithFormat:@"Flips: %d", self.flipCount];
    NSLog(@"flipCount changed to %d", self.flipCount);
}

- (IBAction)touchCardButton:(UIButton *)sender
{
    if ([sender.currentTitle length])
    {
        [sender setBackgroundImage:[UIImage imageNamed:@"cardback"]
                          forState:UIControlStateNormal];
        [sender setTitle:@"" forState:UIControlStateNormal];
    }
    else
    {
        [sender setBackgroundImage:[UIImage imageNamed:@"cardfront"] forState:UIControlStateNormal];
        // we should drow a random card from the deck
        // instead of the fixed string, for exercise 6
        // [sender setTitle:@"A♣︎" forState:UIControlStateNormal];
        NSString *btn_str  = @"?";
        Card *rand_card = [self.deck drawRandomCard];
        if (rand_card) {
            btn_str = [rand_card contents];
        }
        [sender setTitle:btn_str forState:UIControlStateNormal];
    }
    
    self.flipCount++;
}

@end
