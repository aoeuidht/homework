//
//  CardGameViewController.h
//  Matchismo
//
//  Created by liszt on 6/17/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import <UIKit/UIKit.h>

#import "Deck.h"

@interface CardGameViewController : UIViewController

- (Deck *)createDeck;
- (IBAction)touchCardButton:(UIButton *)sender;
- (void) updateUI;
- (NSString *) titleForCard:(Card *)card;
- (UIImage *) backgroundImageForCard:(Card *) card;
@end
