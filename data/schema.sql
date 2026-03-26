-- ===========================================================
--  BenchmarkIQ — MySQL Database Schema
--  Companies: Apple Inc. vs Samsung Electronics
--  Data Year: FY 2023
--  Sources: Apple 10-K, Samsung Annual Report, IDC,
--           Glassdoor, ACSI, Bain, USPTO, Interbrand
-- ===========================================================

CREATE DATABASE IF NOT EXISTS benchmarkiq
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE benchmarkiq;

-- -----------------------------------------------------------
--  1. COMPANIES (master table)
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS companies (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    company_id    VARCHAR(50)  NOT NULL UNIQUE,
    company_name  VARCHAR(120) NOT NULL,
    ticker        VARCHAR(20),
    industry      VARCHAR(80),
    founded       YEAR,
    headquarters  VARCHAR(200),
    logo_color    VARCHAR(10),
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------
--  2. FINANCIAL METRICS
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS financial_metrics (
    id                         INT AUTO_INCREMENT PRIMARY KEY,
    company_id                 VARCHAR(50) NOT NULL,
    data_year                  YEAR        NOT NULL,
    revenue                    DECIMAL(10,2) COMMENT 'USD Billions',
    gross_profit               DECIMAL(10,2) COMMENT 'USD Billions',
    net_income                 DECIMAL(10,2) COMMENT 'USD Billions',
    profit_margin              DECIMAL(6,2)  COMMENT 'Percentage',
    market_cap                 DECIMAL(10,2) COMMENT 'USD Billions',
    market_share_smartphones   DECIMAL(5,2)  COMMENT 'Percentage – IDC Q4 2023',
    operating_margin           DECIMAL(6,2)  COMMENT 'Percentage',
    operating_expenses         DECIMAL(10,2) COMMENT 'USD Billions',
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

-- -----------------------------------------------------------
--  3. PERFORMANCE METRICS
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS performance_metrics (
    id                      INT AUTO_INCREMENT PRIMARY KEY,
    company_id              VARCHAR(50) NOT NULL,
    data_year               YEAR        NOT NULL,
    revenue_growth_yoy      DECIMAL(7,2)  COMMENT 'YoY % change',
    net_income_growth       DECIMAL(7,2)  COMMENT 'YoY % change',
    revenue_per_employee    DECIMAL(8,3)  COMMENT 'USD Millions per employee',
    return_on_equity        DECIMAL(8,2)  COMMENT 'Percentage',
    asset_turnover          DECIMAL(5,2)  COMMENT 'Ratio',
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

-- -----------------------------------------------------------
--  4. INTERNAL / HR METRICS
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS internal_metrics (
    id                    INT AUTO_INCREMENT PRIMARY KEY,
    company_id            VARCHAR(50) NOT NULL,
    data_year             YEAR        NOT NULL,
    total_employees       INT           COMMENT 'Headcount',
    employee_growth_yoy   DECIMAL(6,2)  COMMENT 'YoY % change',
    glassdoor_rating      DECIMAL(3,1)  COMMENT '1–5 Glassdoor scale',
    avg_salary_usd        INT           COMMENT 'Annual USD',
    female_workforce_pct  DECIMAL(5,2)  COMMENT 'Percentage',
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

-- -----------------------------------------------------------
--  5. CUSTOMER METRICS
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS customer_metrics (
    id                    INT AUTO_INCREMENT PRIMARY KEY,
    company_id            VARCHAR(50) NOT NULL,
    data_year             YEAR        NOT NULL,
    nps_score             INT           COMMENT '-100 to 100 – Bain 2023',
    csat_score            DECIMAL(4,1)  COMMENT '1–10 – ACSI 2023',
    brand_value_usd       DECIMAL(10,2) COMMENT 'USD Billions – Interbrand 2023',
    retention_rate_pct    DECIMAL(5,2)  COMMENT 'Percentage',
    positive_reviews_pct  DECIMAL(5,2)  COMMENT 'Percentage',
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

-- -----------------------------------------------------------
--  6. INNOVATION METRICS
-- -----------------------------------------------------------
CREATE TABLE IF NOT EXISTS innovation_metrics (
    id                    INT AUTO_INCREMENT PRIMARY KEY,
    company_id            VARCHAR(50) NOT NULL,
    data_year             YEAR        NOT NULL,
    rd_spending           DECIMAL(8,2)  COMMENT 'USD Billions',
    rd_pct_of_revenue     DECIMAL(5,2)  COMMENT 'Percentage',
    patents_filed         INT           COMMENT 'USPTO filings 2023',
    new_products_launched INT,
    tech_adoption_index   DECIMAL(4,1)  COMMENT '1–10 composite index',
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

-- ===========================================================
--  SEED DATA
-- ===========================================================

INSERT INTO companies
  (company_id, company_name, ticker, industry, founded, headquarters, logo_color)
VALUES
  ('apple',   'Apple Inc.',          'AAPL',      'Technology', 1976, 'Cupertino, CA, USA',  '#60A5FA'),
  ('samsung', 'Samsung Electronics', '005930.KS', 'Technology', 1969, 'Suwon, South Korea',  '#F472B6');

INSERT INTO financial_metrics
  (company_id, data_year, revenue, gross_profit, net_income, profit_margin, market_cap, market_share_smartphones, operating_margin, operating_expenses)
VALUES
  ('apple',   2023, 383.3, 169.1,  97.0, 25.3, 2994.0, 18.8, 29.8, 54.8),
  ('samsung', 2023, 224.0,  64.7,  13.6,  6.1,  374.0, 19.4,  4.9, 46.2);

INSERT INTO performance_metrics
  (company_id, data_year, revenue_growth_yoy, net_income_growth, revenue_per_employee, return_on_equity, asset_turnover)
VALUES
  ('apple',   2023,  -2.8,  -2.8, 2.390, 147.9, 1.09),
  ('samsung', 2023, -14.3, -72.6, 0.820,   4.8, 0.61);

INSERT INTO internal_metrics
  (company_id, data_year, total_employees, employee_growth_yoy, glassdoor_rating, avg_salary_usd, female_workforce_pct)
VALUES
  ('apple',   2023, 161000, -1.0, 4.2, 175000, 35),
  ('samsung', 2023, 270372, -2.1, 3.8,  68000, 28);

INSERT INTO customer_metrics
  (company_id, data_year, nps_score, csat_score, brand_value_usd, retention_rate_pct, positive_reviews_pct)
VALUES
  ('apple',   2023, 72, 8.5, 297.5, 92, 88),
  ('samsung', 2023, 48, 7.4,  91.4, 74, 78);

INSERT INTO innovation_metrics
  (company_id, data_year, rd_spending, rd_pct_of_revenue, patents_filed, new_products_launched, tech_adoption_index)
VALUES
  ('apple',   2023, 29.9, 7.8,  2468, 12, 9.1),
  ('samsung', 2023, 21.2, 9.5,  8513, 28, 8.3);
