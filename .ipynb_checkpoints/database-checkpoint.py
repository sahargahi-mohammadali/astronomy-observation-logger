def save_to_db(self, cursor, conn):
    cursor.execute("""
    INSERT INTO observation
    (target, observer, filter_name, exposure)
    VALUES(?,?,?,?)""",
                  (self.target,
                  self.observer,
                  self.filter,
                  self.exposure))
    conn.commit()