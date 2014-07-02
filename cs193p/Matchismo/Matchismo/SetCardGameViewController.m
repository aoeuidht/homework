//
//  SetCardGameViewController.m
//  Matchismo
//
//  Created by liszt on 7/1/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import "SetCardGameViewController.h"
#import "GameScoreViewController.h"

#import "model/SetCard.h"
#import "model/SetCardDeck.h"
#import "model/CardMatchingGame.h"

@interface SetCardGameViewController ()
@property (strong, nonatomic) IBOutletCollection(UIButton) NSArray *setBtns;

@property (strong, nonatomic) Deck *deck;
@property (strong, nonatomic) CardMatchingGame *game;
@property (weak, nonatomic) IBOutlet UILabel *scoreLabel;
@property (strong, nonatomic) NSMutableArray *score_his;
@end

@implementation SetCardGameViewController

- (void) prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    if ([segue.identifier isEqualToString:@"showHisScore"])
    {
        if ([segue.destinationViewController isKindOfClass:[GameScoreViewController class]])
        {
            GameScoreViewController *gsvc = (GameScoreViewController *)segue.destinationViewController;
            gsvc.score_his = self.score_his;
        }
    }
}

- (IBAction)touchRstBtn:(UIButton *)sender {
    // append his score to the list
    [self.score_his addObject:[NSString stringWithFormat:@"score: %ld",
                               self.game.score]];
    self.deck = Nil;
    self.game = Nil;
    self.scoreLabel.text = @"Score: 0";
    [self updateUI];
}

- (NSMutableArray *) score_his
{
    if (! _score_his)
    {
        _score_his = [[NSMutableArray alloc] init];
    }
    
    return _score_his;
}


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
        NSUInteger cardButtonInedx = [self.setBtns
                                      indexOfObject:cardButton];
        Card *card = [self.game cardAtIndex:cardButtonInedx];
        SetCard *sc = (SetCard *)card;
        if (card.isChosen)
        {
        [cardButton setAttributedTitle:sc.attr_cont
                              forState:UIControlStateNormal];
        }
        else
        {
            [cardButton setAttributedTitle:nil forState:UIControlStateNormal];
            [cardButton setTitle:@""
                        forState:UIControlStateNormal];
            
        }
        [cardButton
         setBackgroundImage:[self backgroundImageForCard:card]
         forState:UIControlStateNormal];
        cardButton.enabled = ! card.isMatched;
    }
}

- (IBAction)setBtnClicked:(UIButton *)sender {
    

    NSLog(@"btn clicked");
    NSUInteger choosenButtonIndex = [self.setBtns
                                      indexOfObject:sender];
    [self.game chooseCardAtIndex:choosenButtonIndex];
    
    self.scoreLabel.text = [NSString stringWithFormat:@"Score: %ld",
                            (long)self.game.score];
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
