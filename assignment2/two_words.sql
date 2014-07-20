select count(*) from (select docid, count(*) from (select docid, term from frequency where term = 'transactions' or term = 'world' group by docid, term) group by docid having count(*) > 1);
