import unittest
from statistics_service import StatisticsService,SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService( PlayerReaderStub() )

    def test_search_player_ok(self):
        p = str(self.stats.search("Lemieux"));
        self.assertMultiLineEqual( p, "Lemieux PIT 45 + 54 = 99")
        
    def test_search_player_notfound(self):
        p = self.stats.search("Mörkö");
        self.assertEqual( p, None)
        
    def test_top_player(self):
        p = str(self.stats.top(1)[0])
        self.assertMultiLineEqual( p, "Gretzky EDM 35 + 89 = 124")
        
    def test_team_members(self):
        p = str(self.stats.team("DET")[0])
        self.assertMultiLineEqual( p, "Yzerman DET 42 + 56 = 98")

    def test_top_goals(self):
        p = str(self.stats.top(3,SortBy.GOALS)[2])
        self.assertMultiLineEqual( p, "Kurri EDM 37 + 53 = 90")
        
    def test_top_assists(self):
        p = str(self.stats.top(3,SortBy.ASSISTS)[1])
        self.assertMultiLineEqual( p, "Yzerman DET 42 + 56 = 98")
        
    def test_top_points(self):
        p = str(self.stats.top(4,SortBy.POINTS)[3])
        self.assertMultiLineEqual( p, "Kurri EDM 37 + 53 = 90")
        
        
