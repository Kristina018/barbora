from models.db import DB
from page_objects.barbora_item_page import BarboraItemPage
import datetime


class BarboraItem:

    def __init__(self, driver):
        # self.title = None
        # self.size = None
        self.driver = driver

    def fill(self):
        bip = BarboraItemPage(self.driver)
        self.title = bip.get_title()
        # self.manufacturer = bip.get_manufacturer()
        self.size = bip.get_size()

    def save(self):
        self.db = DB()
        query = ("INSERT INTO `prekes`(`title`, `manufacturer`, `price`, `unit`, `size`, `property`, `category`, `shop`, `last_updated`) VALUES ("
                 "%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        self.db.conn.cursor().execute(query, (self.title, "m", 3.99, "vnt", self.size, "prop", "categ", "Barbora", "2024-11-24"))
        self.db.conn.commit()
        self.db.close()