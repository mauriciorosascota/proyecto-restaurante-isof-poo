create database preparatoria;
use preparatoria;

--tabla alumnos
create table alumnos(
numerocontrol INT primary key,
nombre nvarchar (100),
edad INT,
añocursa INT,
numMaterias INT,
genero nvarchar (10),
Numtelefono nvarchar (20),
)

INSERT INTO alumnos (NumeroControl, nombre, edad, añoCursa, numMaterias, genero, NumTelefono)
VALUES
    (1, 'Juan Perez', 17, 11, 5, 'Masculino', '123-456-7890'),
    (2, 'Ana Lopez', 16, 10, 4, 'Femenino', '987-654-3210'),
    (3, 'Carlos Ramirez', 18, 12, 6, 'Masculino', '555-555-5555');


--tabla maestros 
create table maestros (
    NumeroMaestro INT PRIMARY KEY,
    Nombre NVARCHAR(100),
    Edad INT,
    GradoEstudios NVARCHAR(50),
    NumTelefono NVARCHAR(20)
);

INSERT INTO maestros (NumeroMaestro, Nombre, Edad, GradoEstudios, NumTelefono)
VALUES
    (101, 'Maria Garcia', 35, 'Maestrú} en Educación', '111-222-3333'),
    (102, 'Pedro Martinez', 40, 'Doctorado en Matemáticas', '444-555-6666'),
    (103, 'Laura Fernandez', 32, 'Licenciatura en Literatura', '777-888-9999');


--tabla materias 
create table materias (
    ClaveMateria INT PRIMARY KEY,
    NombreMateria NVARCHAR(100)
);

INSERT INTO Materias (ClaveMateria, NombreMateria)
VALUES
    (1, 'Matemáticas'),
    (2, 'Historia'),
    (3, 'Literatura');


--tabla aulas
create table Aulas (
    NumeroAula INT PRIMARY KEY,
    CantidadAlumnos INT
);

INSERT INTO Aulas (NumeroAula, CantidadAlumnos)
VALUES
    (101, 30),
    (102, 25),
    (103, 20);


create table AlumnoMateria ( 
    ID INT PRIMARY KEY IDENTITY,
    NumeroControl INT,
    ClaveMateria INT,
    NumeroMaestro INT,
    NumeroAula INT,
    FOREIGN KEY (NumeroControl) REFERENCES Alumnos(NumeroControl),
    FOREIGN KEY (ClaveMateria) REFERENCES Materias(ClaveMateria),
    FOREIGN KEY (NumeroMaestro) REFERENCES Maestros(NumeroMaestro),
    FOREIGN KEY (NumeroAula) REFERENCES Aulas(NumeroAula)
);

INSERT INTO AlumnoMateria (NumeroControl, ClaveMateria, NumeroMaestro, NumeroAula)
VALUES
    (1, 1, 102, 101),
    (2, 2, 101, 102),
    (3, 3, 103, 103);
	||                                                                                                                                                                                                                                                                                                                                                                                                                  

