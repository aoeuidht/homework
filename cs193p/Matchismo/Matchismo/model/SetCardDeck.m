//
//  SetCardDeck.m
//  Matchismo
//
//  Created by liszt on 7/1/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import "SetCardDeck.h"
#import "SetCard.h"

@implementation SetCardDeck

- (instancetype) init
{
    self = [super init];
    if (self)
    {
        for (NSString *sym in [SetCard validSymbols])
        {
            for (NSString *num in [SetCard validNumbers])
            {
                for (NSString *sha in [SetCard validShadings])
                {
                    for (NSString *col in [SetCard validColors])
                    {
                        SetCard *c = [[SetCard alloc] init];
                        c.symbol = sym;
                        c.number = num;
                        c.shading = sha;
                        c.color = col;
                        [self addCard:c];
                    }
                }
            }
        }
    }
    return self;

}
@end
