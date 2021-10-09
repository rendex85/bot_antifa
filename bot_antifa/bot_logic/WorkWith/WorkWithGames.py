import io
import random

from utils.RegexUtils import compare_chess
from .MainWorkWith import BaseWorkWith
import chess
import chess.svg
from cairosvg import svg2png


class ChessGame:

    def __init__(self, obj):
        self.first_player_id = None
        self.second_player_id = None
        self.current_player_id = None
        self.conference_id = None
        self.move_text = None
        self.board = chess.Board()
        self.obj = obj

    def game_start(self):
        self.first_player_id = self.obj.from_id
        self.conference_id = self.obj.peer_id
        return random.choice(["Вы создали игру! \n Ждем ответа второго игрока...",
                              "Молодец какой, драться хочешь? \n Ждем второго драчуна...",
                              "Начинается дикое хрючелово! \n Где же второй игрок?"])

    def game_accepted(self, second_gamer_id):
        self.second_player_id = second_gamer_id
        self.current_player_id = random.choice([self.second_player_id, self.first_player_id])
        return f"@id{self.current_player_id}(Молодчага) - вы играете за белых, начинайте!", self._generate_desc_picture()

    def check_is_game_must_be_stopped(self):
        if self.board.is_checkmate():
            return "checmate, end match, board"
        elif self.board.is_stalemate():
            return "pat from player, give another player "
        return None

    def _check_is_move_message_correct(self, message_to_move):
        move_text = (message_to_move[5:]).lower()
        if not compare_chess(move_text):
            return None
        return move_text

    def _generate_desc_picture(self):
        svg = chess.svg.board(self.board)
        png_board_bytes = svg2png(bytestring=svg)
        io_file = io.BytesIO(png_board_bytes)
        return io_file

    def do_move(self, message_to_move):
        self.move_text = None
        self.move_text = self._check_is_move_message_correct(message_to_move)
        if not self.move_text:
            self.move_text = None
            return "incorrect_move_text"

        move = chess.Move.from_uci(self.move_text)
        if move not in self.board.legal_moves:
            self.move_text = None
            return "illegal_move"

        self.board.push(move)
        print(self.current_player_id)
        self.current_player_id = self.second_player_id if self.current_player_id == self.first_player_id else self.first_player_id
        print(self.current_player_id)
        return self._generate_desc_picture()

    def __str__(self):
        return str(self.conference_id)
