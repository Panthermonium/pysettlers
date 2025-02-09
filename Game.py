from Board import *
from Player import *
from Building import *
from Cards import *
import random
class Game:
    def __init__(self,playerNum = 3,board_type = "random"):
        self.board = Grid(7)
        if(board_type == 'default'):
            self.board.defaultBoard()
        else:
            if(board_type =="random"):
                self.board.random_board()

        self.resource_cards = {}
        self.development_cards = DevelopmentCards()

        self.players = [Player(1,'RED'), Player(2,'BLUE'),Player(3,'WHITE'),Player(4,'GREEN')]
        # for i in range(playerNum):
        #     self.players.append(Player(i + 1,'RED'))

        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]
        self.current_turn = 0
        self.winner = None
        
    def start_game(self):

        self.current_turn = 1

        while not self.winner:
            print("Starting turn " + str(self.current_turn))
            print("Current player is  " + str(self.current_player.name))
            print(str(self.current_player.resources))

    def check_winner(self):
        for player in self.players:
            if player.victory_points == 10:
                self.winner = player
                print(self.winner)
                return self.winner
            

    def end_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player = self.players[self.current_player_index]
        print("End Turn")
        return self.current_player
    
    def roll_dice(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        roll = dice1 + dice2
        print("Roll this turn", roll)

        rolled_tiles = []
        
        for vert in self.board.vertices.keys():
            if self.board.vertices[vert] != '':
                rolled_tiles = touches(vert)
        
        for tile in rolled_tiles:
            if self.board.tiles[tile].rollNum == roll:
                print(self.board.tiles[tile].resource)
                self.current_player.add_resource(self.board.tiles[tile].resource, 1)
        
        
    
    def place_settlement(self,vertex,player):
           
            if self.current_turn == 0:
                if self.board.vertices[vertex] == '':
                        self.board.vertices.update({vertex: Building(BuildingType.Settlement,player)})
                        player.add_settlement(vertex)
                        player.add_victory_point()
            elif (player.resources.get(TileResource.Brick) >=1) and (player.resources.get(TileResource.Lumber) >=1) and (player.resources.get(TileResource.Wool) >=1) and (player.resources.get(TileResource.Grain) >=1):
                        if self.board.vertices[vertex] == '':
                            self.board.vertices.update({vertex: Building(BuildingType.Settlement,player)})
                            player.add_settlement(vertex)
                            player.remove_resource(TileResource.Brick,1)
                            player.remove_resource(TileResource.Lumber,1)
                            player.remove_resource(TileResource.Wool,1)
                            player.remove_resource(TileResource.Grain,1)
                            player.add_victory_point()
            else:
                raise Exception("Not Enough Resources")            
            
    def place_road(self,edge,player):
        if self.current_turn == 0:
            if self.board.edges[edge] == '':
                        self.board.edges.update({edge: Road(player)})
                        player.add_road(edge)
        elif (player.resources.get(TileResource.Brick) >=1) and (player.resources.get(TileResource.Lumber) >=1):
                    if self.board.edges[edge] == '':
                        if self.edges[edge]:
                            self.board.edges.update({edge: Road(player)})
                            player.add_road(edge)
                            player.remove_resource(TileResource.Brick,1)
                            player.remove_resource(TileResource.Lumber,1)


        
            
                   
                        
        
        else:
            raise Exception("Not Enough Resources")

    def upgrade_settlement(self,vertex,player):
        if player.resources.get((TileResource.Grain >= 2) and (TileResource.Ore >= 3)):
            self.board.vertices.update({vertex: Building(BuildingType.City,player)})
            player.add_city(vertex)
            player.remove_resource(TileResource.Grain,2)
            player.remove_resource(TileResource.Ore,3)
            player.add_victory_point()
            
        else:
            print("Not Enough Resources")
    
    def buy_development_card(self, player):
        if player.resources.get((TileResource.Grain >= 1) and (TileResource.Wool >= 1) and (TileResource.Wool >= 1)):
             drawnCard = self.development_cards.draw_card()
             player.add_development_card(drawnCard)
             player.remove_resource(TileResource.Grain,1)
             player.remove_resource(TileResource.Ore,1)
             player.remove_resource(TileResource.Wool,1)
        else:
             print("Not Enough Resources")



    def print_players_data(self):
        for player in self.players:
            print("Player" ,player.name)
            print(player.resources)
            print("Victory Points", player.victory_points)

    def first_turn(self):
        pass

    def trade_resource(self,current_player):
        pass






def print_board(newgame):
    for tile in newgame.board.tiles.keys():
        if newgame.board.tiles[tile] != 'Water':
            for vert in corners(tile):
                if newgame.board.vertices[vert] !='':
                    print(vert)

