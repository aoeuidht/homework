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
        return [self matchMode2: [otherCards firstObject]];
    }
    else if ([otherCards count] == 2)
    {
        return [self matchMode3:[otherCards firstObject] withCard:otherCards[1]];
    }
    
    return score;
}

- (int) matchMode3:(PlayingCard *) oc1
          withCard:(PlayingCard *) oc2
{
    int score = 0;
    if ((self.rank == oc1.rank) &&
        (self.rank == oc2.rank))
    {
        score = 8;
    }
    else if (([self.suit isEqualToString:oc1.suit]) &&
             ([self.suit isEqualToString:oc2.suit]))
    {
        score = 2;
    }
    NSLog(@"%@ vs %@ vs %@",
          self.contents,
          oc1.contents,
          oc2.contents);
    return score;
}

- (int) matchMode2:(PlayingCard *) otherCard
{
    int score = 0;
    if (self.rank == otherCard.rank)
    {
        score = 4;
    }
    else if ([otherCard.suit isEqualToString:self.suit])
    {
        score = 1;
    }
    NSLog(@"%@ vs %@",
          self.contents,
          otherCard.contents);
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
