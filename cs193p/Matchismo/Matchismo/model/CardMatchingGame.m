//
//  CardMatchingGame.m
//  Matchismo
//
//  Created by liszt on 6/24/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import "CardMatchingGame.h"

@interface CardMatchingGame()
@property (nonatomic, readwrite) NSInteger score;
@property (nonatomic, readwrite) NSInteger play_mode;
@property (nonatomic, strong) NSMutableArray *cards;
@end

@implementation CardMatchingGame

- (NSMutableArray *)cards
{
    if (! _cards)
    {
        _cards = [[NSMutableArray alloc] init];
    }
    return _cards;
}

- (instancetype) initWithCardCount:(NSUInteger)count
                         usingDeck:(Deck *)deck
                            atMode:(int) play_mode
{
    self = [super init];
    if (self)
    {
        for (int i=0; i < count; i++)
        {
            Card *card = [deck drawRandomCard];
            if (card)
            {
                [self.cards addObject:card];
            }
            else
            {
                self = nil;
                break;
            }
        }
        self.play_mode = play_mode;
    }
    return self;
}

- (Card *) cardAtIndex:(NSUInteger)index
{
    return (index < [self.cards count]) ? self.cards[index] : nil;
}

static const int MISMATCH_PENALTY = 2;
static const int MATCH_BOUNS = 4;
static const int COST_TO_CHOOSE = 1;

- (void) chooseCardAtIndex:(NSUInteger)index
{
    Card *card = [self cardAtIndex:index];
    if (! card.isMatched)
    {
        if (card.isChosen)
        {
            card.chosen = NO;
        }
        else
        {
            NSMutableArray *selectCards = [[NSMutableArray alloc] init];
            for (Card *otherCard in self.cards)
            {
                if (otherCard.isChosen &&
                    (! otherCard.isMatched))
                {
                    [selectCards addObject:otherCard];
                }
            }
            if ([selectCards count] == (self.play_mode - 1))
            {
                int matchScore = [card match:selectCards];
                if (matchScore)
                {
                    self.score += matchScore * MATCH_BOUNS;
                    for (Card *otherCard in selectCards)
                    {
                        otherCard.matched = YES;
                    }
                    card.matched = YES;
                }
                else
                {
                    self.score -= MISMATCH_PENALTY;
                    for (Card *otherCard in selectCards)
                    {
                        otherCard.chosen = NO;
                    }
                }
            }
            card.chosen = YES;
            self.score = self.score - COST_TO_CHOOSE;
        }
    }
}

@end
