ALTER TABLE empresas MODIFY cnpj VARCHAR(14);

INSERT INTO empresas 
    (nome, cnpj)
VALUES
    ('Bradesco', 95614437000121),
    ('Vale', 30753545000130),
    ('Cielo', 70054819000117);

DESC empresas;
DESC prefeitos;
SELECT * FROM empresas;
SELECT * FROM cidades;

INSERT INTO empresas_unidades 
    (empresa_id, cidade_id, sede)
VALUES 
    (1, 1, 1),
    (2, 1, 0),
    (1, 2, 0),
    (2, 2, 1);