//
//  SetCardGameViewController.m
//  Matchismo
//
//  Created by liszt on 7/1/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import "SetCardGameViewController.h"

#import "model/SetCardDeck.h"
#import "model/CardMatchingGame.h"

@interface SetCardGameViewController ()
@property (strong, nonatomic) IBOutletCollection(UIButton) NSArray *setBtns;

@property (strong, nonatomic) Deck *deck;
@property (strong, nonatomic) CardMatchingGame *game;

@end

@implementation SetCardGameViewController


- (CardMatchingGame *) game
{
    if (! _game)
    {
        _game = [[CardMatchingGame alloc]
                 initWithCardCount:[self.setBtns count]
                 usingDeck:[self createDeck]
                 atMode: 3];
    }
    return _game;
}

- (Deck *)createDeck
{
    return [[SetCardDeck alloc] init];
}

- (void) updateUI
{
    for (UIButton *cardButton in self.setBtns)
    {
        int cardButtonInedx = [self.setBtns
                               indexOfObject:cardButton];
        Card *card = [self.game cardAtIndex:cardButtonInedx];
        [cardButton setTitle:[self titleForCard:card] forState:UIControlStateNormal];
        [cardButton
         setBackgroundImage:[self backgroundImageForCard:card]
         forState:UIControlStateNormal];
        cardButton.enabled = ! card.isMatched;
    }
}

- (IBAction)setBtnClicked:(UIButton *)sender {
    

    NSLog(@"btn clicked");
    int choosenButtonIndex = [self.setBtns
                              indexOfObject:sender];
    [self.game chooseCardAtIndex:choosenButtonIndex];
    [self updateUI];

}

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
