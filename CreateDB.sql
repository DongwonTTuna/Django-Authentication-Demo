DROP DATABASE "purchase";

CREATE DATABASE "purchase" WITH OWNER = postgres ENCODING = 'UTF8';

DROP TABLE IF EXISTS CATEGORY;

CREATE TABLE CATEGORY (
    id serial PRIMARY KEY NOT NULL,
    c_name text NOT NULL
);

DROP TABLE IF EXISTS PRODUCTS;

CREATE TABLE PRODUCTS (
    id serial PRIMARY KEY NOT NULL,
    category int NOT NULL,
    p_name text NOT NULL,
    p_desc text,
    avaliable boolean NOT NULL
);

DROP TABLE IF EXISTS USERS;

CREATE TABLE USERS (
    id serial PRIMARY KEY NOT NULL,
    user_id text NOT NULL,
    user_password text NOT NULL,
    user_email text NOT NULL,
    user_address text[] NOT NULL,
    orders int[]
);

DROP TABLE IF EXISTS ORDERS;

CREATE TABLE ORDERS (
    id int NOT NULL PRIMARY KEY,
    tstamp text NOT NULL,
    u_id int NOT NULL,
    b_id int[] NOT NULL
);

DROP PROCEDURE IF EXISTS AP;

CREATE PROCEDURE AP (cn int, pn text, pd text)
LANGUAGE SQL
AS $$
    INSERT INTO PRODUCTS (category, p_name, p_desc, avaliable)
        VALUES (cn, pn, pd, TRUE);
$$;

DROP PROCEDURE IF EXISTS DP;

CREATE PROCEDURE DP (i int)
LANGUAGE SQL
AS $$
    DELETE FROM PRODUCTS
    WHERE id = i;
$$;

DROP PROCEDURE IF EXISTS AO;

CREATE PROCEDURE AO (u_id int, b_id int[])
LANGUAGE SQL
AS $$
    INSERT INTO ORDERS (tstamp, u_id, b_id)
        VALUES (CURRENT_TIMESTAMP, u_id, b_id)
$$;

DROP PROCEDURE IF EXISTS RO;

CREATE PROCEDURE RO (u_id int, o_id int)
LANGUAGE SQL
AS $$
    DELETE FROM ORDERS
    WHERE (id, u_id) = (o_id, u_id);
$$;

DROP PROCEDURE IF EXISTS AU;

CREATE PROCEDURE AU (ui text, up text, ue text, ua text[])
LANGUAGE SQL
AS $$
    INSERT INTO USERS (user_id, user_password, user_email, user_address)
        VALUES (ui, up, ue, ua);
$$;

DROP PROCEDURE IF EXISTS DU;

CREATE PROCEDURE DU (ui text, up text)
LANGUAGE plpgsql
AS $$
DECLARE
    u_id int;
ORDER int;
BEGIN
    SELECT
        id
    FROM
        USERS
    WHERE (user_id, user_password) = (ui, up) INTO u_id;
    FOR
ORDER IN
SELECT
    id
FROM
    ORDERS
WHERE
    u_id = u_id LOOP
        EXECUTE 'DELETE FROM ORDERS WHERE u_id = ''' || u_id || '''';
    END LOOP;
    EXECUTE 'DELETE FROM USERS WHERE (user_id, user_password) = (''' || ui || ''',''' || up || ''')';
END;
$$;

