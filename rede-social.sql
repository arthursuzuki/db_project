create database rede_social;
use rede_social;

CREATE TABLE Usuario (
    id INT PRIMARY key auto_increment,
    email VARCHAR(255) CHECK (email like '%@%.%'),
    nome VARCHAR(255)
);


CREATE TABLE Professor (
    id INT PRIMARY key,
    FOREIGN KEY (id) REFERENCES Usuario(id)
);


CREATE TABLE Aluno (
    id INT PRIMARY key,
    ano_escolar INT check (ano_escolar between 1 and 12),
    fk_escola_id INT,
    FOREIGN KEY (fk_escola_id) REFERENCES Escola(id),
    FOREIGN KEY (id) REFERENCES Usuario(id)
);


CREATE TABLE Grupo (
    id INT PRIMARY key auto_increment,
    nome VARCHAR(255),
    descricao TEXT,
    fk_professor_id INT,
    FOREIGN KEY (fk_professor_id) REFERENCES Professor(id)
);


CREATE TABLE Escola (
    id INT PRIMARY key auto_increment,
    nome VARCHAR(255),
    tipo VARCHAR(50) CHECK (tipo IN ('publica', 'privada'))
);


CREATE TABLE Disciplina (
    id INT PRIMARY key auto_increment,
    nome VARCHAR(255)
);


CREATE TABLE Olimpiada (
    id INT PRIMARY key auto_increment,
    nome VARCHAR(255),
    estado VARCHAR(50),
    cidade VARCHAR(50),
    rua VARCHAR(255),
    numero VARCHAR(50),
    edicao INT 
);


CREATE TABLE Post (
    id INT PRIMARY key auto_increment,
    conteudo TEXT,
    data_post Date,
    fk_usuario_id INT,
    FOREIGN KEY (fk_usuario_id) REFERENCES Usuario(id)
);


CREATE TABLE Comentarios (
    id INT PRIMARY key auto_increment,
    conteudo TEXT,
    data_comentario DATE,
    fk_comentarios_id INT,
    fk_post_id INT,
    fk_usuario_id INT,
    FOREIGN KEY (fk_comentarios_id) REFERENCES Comentarios(id),
    FOREIGN KEY (fk_post_id) REFERENCES Post(id),
    FOREIGN KEY (fk_usuario_id) REFERENCES Usuario(id)
);


CREATE TABLE grupo_disciplina (
    fk_grupo_id INT,
    fk_disciplina_id INT,
    PRIMARY KEY (fk_grupo_id, fk_disciplina_id),
    FOREIGN KEY (fk_grupo_id) REFERENCES Grupo(id),
    FOREIGN KEY (fk_disciplina_id) REFERENCES Disciplina(id)
);

CREATE TABLE participa (
    fk_usuario_id INT,    
	fk_grupo_id INT,
    PRIMARY KEY (fk_usuario_id, fk_grupo_id),
    FOREIGN KEY (fk_grupo_id) REFERENCES Grupo(id),
    FOREIGN KEY (fk_usuario_id) REFERENCES Usuario(id)
);

CREATE TABLE prof_disciplina (
    fk_professor_id INT,
    fk_disciplina_id INT,
    PRIMARY KEY (fk_professor_id, fk_disciplina_id),
    FOREIGN KEY (fk_professor_id) REFERENCES Professor(id),
    FOREIGN KEY (fk_disciplina_id) REFERENCES Disciplina(id)
);

CREATE TABLE leciona (
    fk_professor_id INT,
    fk_escola_id INT,
    PRIMARY KEY (fk_professor_id, fk_escola_id),
    FOREIGN KEY (fk_professor_id) REFERENCES Professor(id),
    FOREIGN KEY (fk_escola_id) REFERENCES Escola(id)
);


CREATE TABLE assiste (
    fk_aluno_id INT,
    fk_professor_id INT,
    fk_escola_id INT,
    PRIMARY KEY (fk_aluno_id, fk_professor_id, fk_escola_id),
    FOREIGN KEY (fk_aluno_id) REFERENCES Aluno(id),
    FOREIGN KEY (fk_professor_id) REFERENCES Professor(id),
    FOREIGN KEY (fk_escola_id) REFERENCES Escola(id)
);


CREATE TABLE concorre (
    fk_aluno_id INT,
    fk_olimpiada_id INT,
    PRIMARY KEY (fk_aluno_id, fk_olimpiada_id),
    FOREIGN KEY (fk_aluno_id) REFERENCES Aluno(id),
    FOREIGN KEY (fk_olimpiada_id) REFERENCES Olimpiada(id)
);


CREATE TABLE olimpiada_disciplina (
    fk_olimpiada_id INT,
    fk_disciplina_id INT,
    PRIMARY KEY (fk_olimpiada_id, fk_disciplina_id),
    FOREIGN KEY (fk_olimpiada_id) REFERENCES Olimpiada(id),
    FOREIGN KEY (fk_disciplina_id) REFERENCES Disciplina(id)
);

INSERT INTO Usuario (email, nome)
VALUES
('maria.silva@email.com', 'Maria Silva'),
('joao.souza@email.com', 'João Souza'),
('ana.costa@email.com', 'Ana Costa'),
('pedro.santos@email.com', 'Pedro Santos'),
('paula.pereira@email.com', 'Paula Pereira'),
('carlos.martins@email.com', 'Carlos Martins'),
('luciana.oliveira@email.com', 'Luciana Oliveira'),
('rafael.araujo@email.com', 'Rafael Araujo');

INSERT INTO Professor (id)
SELECT id FROM Usuario LIMIT 4;

INSERT INTO Aluno (id, ano_escolar, fk_escola_id)
Values
(6, 9, 1),
(7, 9, 1),
(8, 9, 2),
(9, 9, 3),
(10, 9, 4);

/*
truncate table concorre; 

drop table aluno;
drop table concorre ;
drop table assiste;
*/


INSERT INTO Grupo (nome, descricao, fk_professor_id)
VALUES
('Grupo de Matemática', 'Grupo para estudos de matemática', 1),
('Grupo de Português', 'Grupo para estudos de português', 2),
('Grupo de História', 'Grupo para estudos de história', 3),
('Grupo de Química', 'Grupo para estudos de química', 4);

insert into participa (fk_grupo_id, fk_usuario_id)
values
(3, 1),
(4, 2),
(5, 3),
(6, 4),
(3, 2);

INSERT INTO Escola (nome, tipo)
VALUES
('Escola Estadual Colégio Pedro II', 'Pública'),
('Escola Particular Dom Bosco', 'Privada'),
('Escola Técnica Álvaro de Carvalho', 'Pública'),
('Escola de Artes Newton Braga', 'Privada');

INSERT INTO Disciplina (nome)
VALUES
('Matemática'),
('Português'), 
('História'), 
('Química'), 
('Física'), 
('Biologia'),
('Geografia'), 
('Inglês');

INSERT INTO Olimpiada (nome, estado, cidade, rua, numero, edicao)
VALUES
('OBMEP', 'São Paulo', 'São Paulo', 'Rua da Consolação', '2000', 2023),
('Olimpíada Nacional de Língua Portuguesa', 'Rio de Janeiro', 'Rio de Janeiro', 'Avenida Rio Branco', '1', 2023),
('Olimpíada Brasileira de História', 'Minas Gerais', 'Belo Horizonte', 'Avenida Afonso Pena', '500', 2023),
('Olimpíada Brasileira de Química', 'Paraná', 'Curitiba', 'Rua Marechal Floriano Peixoto', '800', 2023);

INSERT INTO Post (conteudo, data_post, fk_usuario_id)
VALUES
('Estou estudando para a Olimpíada Brasileira de Matemática!', '2023-11-15', 1),
('Preciso de ajuda com a gramática portuguesa!', '2023-11-16', 2),
('Estou interessado em saber mais sobre a Segunda Guerra Mundial.', '2023-11-17', 3),
('Adoro química e quero me preparar para a olimpíada!', '2023-11-18', 4);

INSERT INTO Comentarios (conteudo, data_comentario, fk_comentarios_id, fk_post_id, fk_usuario_id)
VALUES
('Boa sorte na sua preparação!', '2023-11-15', NULL, 1, 2),
('Posso te ajudar com algumas questões gramaticais.', '2023-11-16', NULL, 2, 1),
('Recomendo o livro ´A Segunda Guerra Mundial´, de Winston Churchill.', '2023-11-17', NULL, 3, 1),
('Tem uma equipe de química na minha escola que pode te ajudar.', '2023-11-18', NULL, 4, 1);

INSERT INTO grupo_disciplina (fk_grupo_id, fk_disciplina_id)
VALUES
(1, 1),
(1, 3),
(2, 2),
(3, 4),
(4, 5);

INSERT INTO prof_disciplina (fk_professor_id, fk_disciplina_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4);

INSERT INTO leciona (fk_professor_id, fk_escola_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4);

INSERT INTO assiste (fk_aluno_id, fk_professor_id, fk_escola_id)
VALUES
(7, 1, 1),
(8, 2, 2),
(9, 3, 3),
(10, 4, 4);

INSERT INTO concorre (fk_aluno_id, fk_olimpiada_id)
VALUES
(7, 1),
(8, 2),
(9, 3),
(10, 4);

INSERT INTO olimpiada_disciplina (fk_olimpiada_id, fk_disciplina_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4);