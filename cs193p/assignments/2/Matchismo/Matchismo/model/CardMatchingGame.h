//
//  CardMatchingGame.h
//  Matchismo
//
//  Created by liszt on 6/24/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Deck.h"
#import "Card.h"

@interface CardMatchingGame : NSObject

- (instancetype)initWithCardCount:(NSUInteger)count
                        usingDeck:(Deck *)deck
                           atMode: (int) play_mode;

- (void) chooseCardAtIndex:(NSUInteger)index;
- (Card *)cardAtIndex:(NSUInteger)index;

@property (nonatomic, readonly) NSInteger score;
@property (nonatomic, readonly) NSInteger play_mode;
@property (nonatomic, readonly) NSString *match_info;
@end
