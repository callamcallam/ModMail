import sqlite3


class SqliteAPI:
    def __init__(self):
        self.db = sqlite3.connect('./private/config/database.db')
        self.cursor = self.db.cursor()

    def execute(self, sql, values: tuple = None, fetch: bool = False, commit: bool = False):
        if values:
            self.cursor.execute(sql, values)
        else:
            self.cursor.execute(sql)
        if commit:
            self.db.commit()
        if fetch:
            return self.cursor.fetchall()
                
    def fetch_token(self):
        token = self.cursor.execute("SELECT token FROM config;")[0][0] # Will return a tuple, so we need to get the first element of the tuple which this does.
        return token
    
    def fetch_prefix(self):
        prefix = self.cursor.execute("SELECT prefix FROM config;")[0][0]
        return prefix
    
    def fetch_guild_id(self):
        guild_id = self.cursor.execute("SELECT guild_id FROM config;")[0][0]
        return guild_id
    
    def fetch_status(self):
        status = self.cursor.execute("SELECT status FROM config;")[0][0]
        return status
    
    def fetch_game_type(self):
        game_type = self.cursor.execute("SELECT game_type FROM config;")[0][0]
        return game_type
    
    
        