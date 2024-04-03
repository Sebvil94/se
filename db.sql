-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS socket_server;

USE socket_server;

-- Crear la tabla de ciudades
CREATE TABLE IF NOT EXISTS ciudades (
    ciud_id INT AUTO_INCREMENT PRIMARY KEY,
    ciud_nombre VARCHAR(100)
);

-- Crear la tabla de personas
CREATE TABLE IF NOT EXISTS personas (
    dir_tel VARCHAR(15) PRIMARY KEY,
    dir_tipo_tel VARCHAR(20),
    dir_nombre VARCHAR(100),
    dir_direccion VARCHAR(255),
    dir_ciud_id INT,
    FOREIGN KEY (dir_ciud_id) REFERENCES ciudades(ciud_id)
);

-- Insertar datos de prueba en la tabla de ciudades
INSERT INTO ciudades (ciud_nombre) VALUES
('Ciudad A'),
('Ciudad B'),
('Ciudad C'),
('Ciudad D'),
('Ciudad E');

-- Insertar datos de prueba en la tabla de personas
INSERT INTO personas (dir_tel, dir_tipo_tel, dir_nombre, dir_direccion, dir_ciud_id) VALUES
('111111111', 'Casa', 'Persona 1', 'Dirección 1', 1),
('222222222', 'Trabajo', 'Persona 2', 'Dirección 2', 2),
('333333333', 'Casa', 'Persona 3', 'Dirección 3', 3),
('444444444', 'Trabajo', 'Persona 4', 'Dirección 4', 4),
('555555555', 'Casa', 'Persona 5', 'Dirección 5', 5);
