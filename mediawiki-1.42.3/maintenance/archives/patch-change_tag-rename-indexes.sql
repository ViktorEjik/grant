-- This file is automatically generated using maintenance/generateSchemaChangeSql.php.
-- Source: maintenance/abstractSchemaChanges/patch-change_tag-rename-indexes.json
-- Do not modify this file directly.
-- See https://www.mediawiki.org/wiki/Manual:Schema_changes
DROP  INDEX change_tag_rc_tag_id ON  /*_*/change_tag;
CREATE UNIQUE INDEX ct_rc_tag_id ON  /*_*/change_tag (ct_rc_id, ct_tag_id);
DROP  INDEX change_tag_log_tag_id ON  /*_*/change_tag;
CREATE UNIQUE INDEX ct_log_tag_id ON  /*_*/change_tag (ct_log_id, ct_tag_id);
DROP  INDEX change_tag_rev_tag_id ON  /*_*/change_tag;
CREATE UNIQUE INDEX ct_rev_tag_id ON  /*_*/change_tag (ct_rev_id, ct_tag_id);
DROP  INDEX change_tag_tag_id_id ON  /*_*/change_tag;
CREATE INDEX ct_tag_id_id ON  /*_*/change_tag (    ct_tag_id, ct_rc_id, ct_rev_id, ct_log_id  );