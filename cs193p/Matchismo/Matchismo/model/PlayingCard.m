//
//  PlayingCard.m
//  Matchismo
//
//  Created by liszt on 6/17/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import "PlayingCard.h"

@implementation PlayingCard

- (NSString *) contents
{
    NSArray *rantStrings = [PlayingCard rankStrings];
    return [rantStrings[self.rank]
            stringByAppendingString:self.suit];
}

- (int) match:(NSArray *)otherCards
{
    int score = 0;
    if ([otherCards count] == 1)
    {
        PlayingCard *otherCard = [otherCards firstObject];
        if (self.rank == otherCard.rank)
        {
            score = 4;
        }
        else if ([otherCard.suit isEqualToString:self.suit])
        {
            score = 1;
        }
    }
    return score;
}

@synthesize suit = _suit;

+ (NSArray *) validSuits
{
    return @[@"♠︎",  @"♣︎", @"♥︎", @"♦︎"];
}

+ (NSArray *) rankStrings
{
    return @[@"?", @"A", @"2", @"3", @"4", @"5", @"6",
             @"7", @"8", @"9", @"10", @"J", @"Q", @"K"];
}

- (NSString *) suit
{
    return _suit ? _suit : @"?";
}

- (void)setSuit:(NSString *)suit
{
    if ([[PlayingCard validSuits] containsObject:suit])
    {
        _suit = suit;
    }
}

+ (NSUInteger) maxRank
{
    return [[self rankStrings] count] - 1;
}

- (void) setRank:(NSUInteger)rank
{
    if (rank <= [PlayingCard maxRank]) {
        _rank = rank;
    }
}
@end
