#!/usr/bin/python3
class DBInfo:
    def __init__(self, ip, port, db_name, user, paswd):
        self.ip: str = ip
        self.port: str = port
        self.db_name: str = db_name
        self.user: str = user
        self.paswd: str = paswd



db_auth = DBInfo("ec2-3-222-30-53.compute-1.amazonaws.com", "5432", "d9i05h7i78ht63",
                 "ivipfsifsguaeg", "44df42a96145dbb51d560637209323426da5dab23e50b5fb6244de8bb8bd595a")
