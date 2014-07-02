//
//  GameScoreViewController.m
//  Matchismo
//
//  Created by liszt on 7/2/14.
//  Copyright (c) 2014 Llhf. All rights reserved.
//

#import "GameScoreViewController.h"

@interface GameScoreViewController ()
@property (weak, nonatomic) IBOutlet UITextView *gameScoreText;

@end

@implementation GameScoreViewController

- (void) setScore_his:(NSMutableArray *)score_his
{
    _score_his = score_his;
    if (self.view.window)
    {
        [self updateUI];
    }
}

- (void) updateUI
{
    NSString *rst = @"";
    
    if (_score_his) {
        NSLog(@"we got non-empty score his");
        rst = [self.score_his componentsJoinedByString:@"\n"]; // cennect the score his together
    }
    
    self.gameScoreText.text = rst;
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
    [self updateUI];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
