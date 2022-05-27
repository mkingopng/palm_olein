-- Table: public.price

-- DROP TABLE IF EXISTS public.price;

CREATE TABLE IF NOT EXISTS public.price
(
    "DAILY PRICES" date,
    "Palm olein RBD Mal FOB US$" double precision
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.price
    OWNER to mkingston;