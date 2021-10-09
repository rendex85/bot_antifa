import io

from EventHandler.HandlerKernel import BaseHandler
from WorkWith.WorkWithGames import ChessGame
from utils.WorkWithUtils.WorkWithAuth import AuthTools
from utils.WorkWithUtils.WorkWithUpload import PhotoUpload


class ChessStart(BaseHandler):
    trigger_strict = ["!шахматы", ]

    def preHandler(self):
        chess_object: ChessGame = None
        for el in self.dict_of_globals["chess_objects_list"]:
            if el.conference_id == self.obj.peer_id:
                if not el.second_player_id and el.first_player_id != self.obj.from_id:
                    chess_object = el
                else:
                    self.message_data.message = "Ты че дурррак блять???"
                    return
                break
        if not chess_object:
            chess_object = ChessGame(self.obj)
            self.message_data.message = chess_object.game_start()
            self.dict_of_globals["chess_objects_list"].append(chess_object)
        else:
            message, png_bytes_desk = chess_object.game_accepted(self.obj.from_id)
            attachment = PhotoUpload.load_img_from_local_data(AuthTools.authByGroup()[2], png_bytes_desk)
            self.message_data.message, self.message_data.attachment = message, attachment


class ChessMove(BaseHandler):
    trigger_in = ["!ход", ]

    def preHandler(self):
        chess_object: ChessGame = None
        for index_chess, el in enumerate(self.dict_of_globals["chess_objects_list"]):
            if el.conference_id == self.obj.peer_id:
                if el.current_player_id == self.obj.from_id:
                    chess_object = el
                else:
                    self.message_data.message = "Ты балбес, так делать нельзя"
                    return
                break
        if not chess_object:
            self.message_data.message = "А ты игру сначала начни, а потом уже ходи, умник"
            return
        else:
            turn_info = chess_object.do_move(self.obj.text)
            if turn_info == "incorrect_move_text":
                self.message_data.message = "Научись нормально писать, а потом ходи"
                return
            elif turn_info == "illegal_move":
                self.message_data.message = "Так ходить нелья"
                return
            else:
                attachment = PhotoUpload.load_img_from_local_data(AuthTools.authByGroup()[2], turn_info)
                if chess_object.check_is_game_must_be_stopped():
                    message = f"Игра закончена! Победил @id{self.obj.from_id}(Молодчага)!"
                    self.message_data.message, self.message_data.attachment = message, attachment
                    self.dict_of_globals["chess_objects_list"].pop(index_chess)
                else:
                    message = f"Ход {chess_object.move_text} совершен. Теперь ходишь @id{chess_object.current_player_id}(ты)"
                    self.message_data.message, self.message_data.attachment = message, attachment


class SurrenderChess(BaseHandler):
    trigger_strict = ["!сдаться", ]

    def preHandler(self):
        chess_object: ChessGame = None
        for index_chess, el in enumerate(self.dict_of_globals["chess_objects_list"]):
            if el.conference_id == self.obj.peer_id:
                if el.current_player_id == self.obj.from_id:
                    chess_object = el
                else:
                    self.message_data.message = "Ты балбес, так делать нельзя"
                    return
                break
        if not chess_object:
            self.message_data.message = "А ты игру сначала начни, а потом уже ходи, умник"
            return
        else:
            winner = chess_object.first_player_id if chess_object.first_player_id != self.obj.from_id else chess_object.second_player_id
            desk = chess_object._generate_desc_picture()
            message = f"Игра закончена! Игрок @id{self.obj.from_id}(сдался), победил @id{winner}(Молодчага)!"
            attachment = PhotoUpload.load_img_from_local_data(AuthTools.authByGroup()[2], desk)
            self.dict_of_globals["chess_objects_list"].pop(index_chess)
            self.message_data.message, self.message_data.attachment = message, attachment
