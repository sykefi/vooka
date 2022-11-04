-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler version: 0.9.4
-- PostgreSQL version: 13.0
-- Project Site: pgmodeler.io
-- Model Author: ---

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
	kaavatunnus uuid,
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

-- object: kaavatiedot."Kaavasuositus" | type: TABLE --
-- DROP TABLE IF EXISTS kaavatiedot."Kaavasuositus" CASCADE;
CREATE TABLE kaavatiedot."Kaavasuositus" (
	id bigint NOT NULL,
	elinkaaren_tila varchar(2),
	kaavoitusteema varchar(2),
	suositusnumero bigint,
	voimassaoloaika varchar,
	arvo varchar,
	"id_Kaava" bigint,
	CONSTRAINT "PK_kaavasuositus" PRIMARY KEY (id)
);
-- ddl-end --
COMMENT ON TABLE kaavatiedot."Kaavasuositus" IS E'Kaavaan sisältyvä ei-velvoittava ohje, joka ilmentää esimerkiksi toteutuksen tapaa ja tavoitetta.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaavasuositus".elinkaaren_tila IS E'Elinkaaren tila, jossa kaavan versio on.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaavasuositus".kaavoitusteema IS E'Kaavoituksen piiriin kuuluva temaattinen aihealue.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaavasuositus".suositusnumero IS E'Kaavasuosituksen suositusnumero';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaavasuositus".voimassaoloaika IS E'Aikaväli, jona asiasta tehty päätös suunnitelmineen ja säännöksineen on lainvoimainen.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaavasuositus".arvo IS E'Kaavasuosituksen lajia tarkentava tekstiarvo';
-- ddl-end --
ALTER TABLE kaavatiedot."Kaavasuositus" OWNER TO postgres;
-- ddl-end --

-- object: "Kaava_fk" | type: CONSTRAINT --
-- ALTER TABLE kaavatiedot."Kaavasuositus" DROP CONSTRAINT IF EXISTS "Kaava_fk" CASCADE;
ALTER TABLE kaavatiedot."Kaavasuositus" ADD CONSTRAINT "Kaava_fk" FOREIGN KEY ("id_Kaava")
REFERENCES kaavatiedot."Kaava" (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: kaavatiedot."Kaavan_kumoamistieto" | type: TABLE --
-- DROP TABLE IF EXISTS kaavatiedot."Kaavan_kumoamistieto" CASCADE;
CREATE TABLE kaavatiedot."Kaavan_kumoamistieto" (
	id bigint NOT NULL,
	kumottavan_kaavan_tunnus varchar,
	kumoaa_kaavan_kokonaan boolean,
	kumottavan_kaavan_alue geometry(POLYGON, 3067),
	kumottavan_maarayksen_tunnus varchar,
	kumottavan_suosituksen_tunnus varchar,
	"id_Kaava" bigint,
	CONSTRAINT "PK_kaavan_kumoamistieto" PRIMARY KEY (id)
);
-- ddl-end --
COMMENT ON TABLE kaavatiedot."Kaavan_kumoamistieto" IS E'Tieto kaavan hyväksymisen johdosta kumoutuvasta aiemmasta kaavasta, sen sisältämistä yksittäisistä kaavamääräyskohteista tai kaavamääräyksistä.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaavan_kumoamistieto".kumottavan_kaavan_tunnus IS E'Sen kaavan kaavatunnus, joka kumotaan kokonaan tai osittain tämän kaavan tullessa voimaan.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaavan_kumoamistieto".kumoaa_kaavan_kokonaan IS E'Viitattu kaava kumoutuu kokonaisuudessaan tämän kaavan tullessa voimaan.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaavan_kumoamistieto".kumottavan_kaavan_alue IS E'Aluemainen geometria, joka rajaa viitattavan kaavan osan, johon kohdistetut kaavakohteet ja -määräykset kumoutuvat.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaavan_kumoamistieto".kumottavan_maarayksen_tunnus IS E'Viittaustunnus kumottavalle kaavamääräykselle, joka sisältyy kumottavaan kaavaan.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Kaavan_kumoamistieto".kumottavan_suosituksen_tunnus IS E'Viittaustunnus kumottavalle kaavasuositukselle, joka sisältyy kumottavaan kaavaan.';
-- ddl-end --
ALTER TABLE kaavatiedot."Kaavan_kumoamistieto" OWNER TO postgres;
-- ddl-end --

-- object: "Kaava_fk" | type: CONSTRAINT --
-- ALTER TABLE kaavatiedot."Kaavan_kumoamistieto" DROP CONSTRAINT IF EXISTS "Kaava_fk" CASCADE;
ALTER TABLE kaavatiedot."Kaavan_kumoamistieto" ADD CONSTRAINT "Kaava_fk" FOREIGN KEY ("id_Kaava")
REFERENCES kaavatiedot."Kaava" (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "Kaavan_kumoamistieto_uq" | type: CONSTRAINT --
-- ALTER TABLE kaavatiedot."Kaavan_kumoamistieto" DROP CONSTRAINT IF EXISTS "Kaavan_kumoamistieto_uq" CASCADE;
ALTER TABLE kaavatiedot."Kaavan_kumoamistieto" ADD CONSTRAINT "Kaavan_kumoamistieto_uq" UNIQUE ("id_Kaava");
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

-- object: kaavatiedot."Osallistumis_ja_arviointisuunnitelma" | type: TABLE --
-- DROP TABLE IF EXISTS kaavatiedot."Osallistumis_ja_arviointisuunnitelma" CASCADE;
CREATE TABLE kaavatiedot."Osallistumis_ja_arviointisuunnitelma" (
	id bigint NOT NULL,
	tiedosto varchar,
	"id_Kaava" bigint,
	CONSTRAINT "PK_osallistumis_ja_arviointisuunnitelma" PRIMARY KEY (id)
);
-- ddl-end --
COMMENT ON TABLE kaavatiedot."Osallistumis_ja_arviointisuunnitelma" IS E'Kaavoituksen alkuvaiheessa laadittava suunnitelma, jossa kuvataan kaavoituksen lähtökohdat ja tavoitteet, suunniteltu aikataulu, osallistumis- ja vuorovaikutusmuodot sekä kaavan vaikutusten arviointitavat.';
-- ddl-end --
COMMENT ON COLUMN kaavatiedot."Osallistumis_ja_arviointisuunnitelma".tiedosto IS E'Liittyvä asiakirja';
-- ddl-end --
ALTER TABLE kaavatiedot."Osallistumis_ja_arviointisuunnitelma" OWNER TO postgres;
-- ddl-end --

-- object: "Kaava_fk" | type: CONSTRAINT --
-- ALTER TABLE kaavatiedot."Osallistumis_ja_arviointisuunnitelma" DROP CONSTRAINT IF EXISTS "Kaava_fk" CASCADE;
ALTER TABLE kaavatiedot."Osallistumis_ja_arviointisuunnitelma" ADD CONSTRAINT "Kaava_fk" FOREIGN KEY ("id_Kaava")
REFERENCES kaavatiedot."Kaava" (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "Osallistumis_ja_arviointisuunnitelma_uq" | type: CONSTRAINT --
-- ALTER TABLE kaavatiedot."Osallistumis_ja_arviointisuunnitelma" DROP CONSTRAINT IF EXISTS "Osallistumis_ja_arviointisuunnitelma_uq" CASCADE;
ALTER TABLE kaavatiedot."Osallistumis_ja_arviointisuunnitelma" ADD CONSTRAINT "Osallistumis_ja_arviointisuunnitelma_uq" UNIQUE ("id_Kaava");
-- ddl-end --


