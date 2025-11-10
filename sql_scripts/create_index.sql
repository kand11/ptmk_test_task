CREATE INDEX idx_gender_fullname
ON employees (
              full_name
              , sex
              , birth_date
 );