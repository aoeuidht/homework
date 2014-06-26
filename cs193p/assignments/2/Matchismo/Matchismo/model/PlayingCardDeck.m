//
//  PlayingCardDeck.m
//  Matchismo
//
//  Created by liszt on 6/17/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import "PlayingCardDeck.h"
#import "PlayingCard.h"

@implementation PlayingCardDeck

- (instancetype) init
{
    self = [super init];
    if (self)
    {
        for (NSString *suit in [PlayingCard validSuits])
        {
            for (NSUInteger rank = 1;
                 rank <= [PlayingCard maxRank];
                 rank++)
            {
                PlayingCard *card = [[PlayingCard alloc] init];
                card.rank = rank;
                card.suit = suit;
                [self addCard:card];
            }
        }
    }
    return self;
}
@end
