-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler version: 0.9.4
-- PostgreSQL version: 13.0
-- Project Site: pgmodeler.io
-- Model Author: Samuli Massinen

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: kaavakanta | type: DATABASE --
-- DROP DATABASE IF EXISTS kaavakanta;
CREATE DATABASE kaavakanta;
-- ddl-end --


-- object: kaavatiedot | type: SCHEMA --
-- DROP SCHEMA IF EXISTS kaavatiedot CASCADE;
CREATE SCHEMA kaavatiedot;
-- ddl-end --
ALTER SCHEMA kaavatiedot OWNER TO postgres;
-- ddl-end --

SET search_path TO pg_catalog,public,kaavatiedot;
-- ddl-end --

-- object: kaavatiedot."Kaava" | type: TABLE --
-- DROP TABLE IF EXISTS kaavatiedot."Kaava" CASCADE;
CREATE TABLE kaavatiedot."Kaava" (
	id bigint NOT NULL,
	kaavatunnus varchar,
	elinkaaren_tila varchar(2),
	kaavalaji varchar(2),
	kaavatiedosto varchar,
	maanalaisuus varchar(2),
	CONSTRAINT "PK_kaava" PRIMARY KEY (id)
);
-- ddl-end --
COMMENT ON TABLE kaavatiedot."Kaava" IS E'Kaavoituksen lopputuloksena syntyvä säännöstö ja suunnitelma, joka on alueellaan maankäytön ja rakentamisen tarkempaa suunnittelua ja toteuttamista juridisesti velvoittava.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaava".elinkaaren_tila IS E'Elinkaaren tila, jossa kaavan versio on.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaava".kaavalaji IS E'Alueiden käytön ohjaustarpeeseen, kaavaan sisältövaatimuksiin, prosessiin ja vastuulliseen hallintoviranomaiseen perustuva luokittelu';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaava".kaavatiedosto IS E'Viittaus kaavatietomallin mukaiseen kaavatiedostoon.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaava".maanalaisuus IS E'Koskeeko kaava maanalaista vai maanpäällistä rakentamista ja maankäyttöä.';
-- ddl-end --
ALTER TABLE kaavatiedot."Kaava" OWNER TO postgres;
-- ddl-end --

-- object: kaavatiedot."Kaavaselostus" | type: TABLE --
-- DROP TABLE IF EXISTS kaavatiedot."Kaavaselostus" CASCADE;
CREATE TABLE kaavatiedot."Kaavaselostus" (
	id bigint NOT NULL,
	tiedosto varchar,
	"id_Kaava" bigint,
	CONSTRAINT "PK_kaavaselostus" PRIMARY KEY (id)
);
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaavaselostus".tiedosto IS E'Kaavaan liittyvä selostus, jossa esitetään kaavan tavoitteiden, mahdollisten vaihtoehtojen ja niiden vaikutusten sekä ratkaisujen perusteiden arvioimiseksi tarpeelliset tiedot.';
-- ddl-end --
ALTER TABLE kaavatiedot."Kaavaselostus" OWNER TO postgres;
-- ddl-end --

-- object: "Kaava_fk" | type: CONSTRAINT --
-- ALTER TABLE kaavatiedot."Kaavaselostus" DROP CONSTRAINT IF EXISTS "Kaava_fk" CASCADE;
ALTER TABLE kaavatiedot."Kaavaselostus" ADD CONSTRAINT "Kaava_fk" FOREIGN KEY ("id_Kaava")
REFERENCES kaavatiedot."Kaava" (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "Kaavaselostus_uq" | type: CONSTRAINT --
-- ALTER TABLE kaavatiedot."Kaavaselostus" DROP CONSTRAINT IF EXISTS "Kaavaselostus_uq" CASCADE;
ALTER TABLE kaavatiedot."Kaavaselostus" ADD CONSTRAINT "Kaavaselostus_uq" UNIQUE ("id_Kaava");
-- ddl-end --


