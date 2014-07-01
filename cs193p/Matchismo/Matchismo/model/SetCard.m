//
//  SetCard.m
//  Matchismo
//
//  Created by liszt on 7/1/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import "SetCard.h"

@implementation SetCard

- (NSString *) contents
{
    return [NSString stringWithFormat:@"%@%@%@%@",
            self.symbol,
            self.number,
            self.shading,
            self.color];
}

static const int MATCH_BOUNS = 4;

- (int) match:(NSArray *)otherCards
{
    int score = 0;
    if ([otherCards count] == 2)
    {
        SetCard *c1 = otherCards[0];
        SetCard *c2 = otherCards[1];
        NSLog(@"try match %@ vs %@ %@",
              self.contents,
              c1.contents,
              c2.contents);
        for (NSString *att in [SetCard validAttrs])
        {
            NSString *a1 = [self valueForKey:att];
            NSString *a2 = [c1 valueForKey:att];
            NSString *a3 = [c2 valueForKey:att];
            if (
                // 3 attribute equal
                ([a1 isEqualToString:a2] &&
                 [a1 isEqualToString:a3]) ||
                // no attribute equal
                ((! [a1 isEqualToString:a2]) &&
                 (! [a1 isEqualToString:a3]) &&
                 (! [a2 isEqualToString:a3])))
            {
                score = score + MATCH_BOUNS;
            }
            else
            {
                score = 0;
                break;
            }
        }
    }
    else
    {
        score = 0;
    }
    
    return score;
}

+ (NSArray *) validAttrs
{
    return @[@"symbol", @"number", @"shading", @"color"];
}

+ (NSArray *) validNumbers
{
    return @[@"1", @"2", @"3"];
}

+ (NSArray *) validSymbols
{
    return @[@"1", @"2", @"3"];
    return @[@"♦︎", @"⚑", @"◼︎"];
}

+ (NSArray *) validColors
{
    return @[@"1", @"2", @"3"];
    return @[@"r", @"g", @"p"];
}

+ (NSArray *) validShadings
{
    return @[@"1", @"2", @"3"];
    return @[@"☐", @"☑︎", @"◼︎"];
}

@end
