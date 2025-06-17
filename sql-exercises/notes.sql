PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE notes (author TEXT, note TEXT);
INSERT INTO notes VALUES('Krzysztof','Zrob pranie.');
INSERT INTO notes VALUES('Adam','Posprzataj pokoj.');
INSERT INTO notes VALUES('Tomasz','Zrob zakupy.');
INSERT INTO notes VALUES('Franek','12345');
COMMIT;
