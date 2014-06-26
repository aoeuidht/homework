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

- (NSString *) chooseCardAtIndex:(NSUInteger)index
{
    NSString *info = @"";
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
                    if (info.length < 1)
                    {
                        info = card.contents;
                    }
                    [selectCards addObject:otherCard];
                    info = [NSString stringWithFormat:@"%@ %@",
                            info,
                            otherCard.contents];
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
                    info = [NSString
                            stringWithFormat:@"Matched %@ for %d points",
                            info,
                            matchScore * MATCH_BOUNS];
                }
                else
                {
                    self.score -= MISMATCH_PENALTY;
                    for (Card *otherCard in selectCards)
                    {
                        otherCard.chosen = NO;
                    }
                    info = [NSString
                            stringWithFormat:@"%@ don't match! %d point penalty!",
                            info,
                            MISMATCH_PENALTY];
                }
            }
            card.chosen = YES;
            self.score = self.score - COST_TO_CHOOSE;
        }
    }
    
    return info;
}

@end
