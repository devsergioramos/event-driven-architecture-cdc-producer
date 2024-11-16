CREATE TABLE package_status (
    id SERIAL PRIMARY KEY,
    actual_address TEXT,
    next_address TEXT,
    status TEXT
);

INSERT INTO public.package_status
(actual_address, next_address, status)
VALUES('78221 Jessica Brook Apt. 400
Walshfort, VT 97992-2156', '34475 Bonnie Bridge Suite 175
South Cynthiachester, IA 25142-2303', 'pending');