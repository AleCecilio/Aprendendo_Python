SELECT e.nome as Empresa, c.nome as Ciddade
FROM empresas e, empresas_unidades eu, cidades c
WHERE e.id = eu.empresa_id
AND c.id = eu.cidade_id
AND sede;

SELECT *
FROM empresas e
INNER JOIN empresas_unidades eu
    ON e.id = eu.empresa_id
INNER JOIN cidades c
    ON c.id = eu.cidade_id
WHERE eu.sede = 1;