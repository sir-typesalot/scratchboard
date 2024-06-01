
CREATE TABLE boards (
    `hash` CHAR(56) NOT NULL,
    `id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(25) NOT NULL,
    `is_active` BOOLEAN DEFAULT 1,
    `create_datetime` DATETIME DEFAULT NOW(),
    PRIMARY KEY (`hash`, `id`)
);

CREATE TABLE board_tags (
    `board_id` INT DEFAULT NULL,
    `tag_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `tag_name` VARCHAR(25) NOT NULL,
    `description` VARCHAR(256) DEFAULT NULL,
    FOREIGN KEY (`board_id`) REFERENCES `boards`(`id`)
);

CREATE TABLE board_tasks (
    `board_id` INT NOT NULL,
    `task_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `tag_id` INT DEFAULT 1,
    `title` VARCHAR(100) NOT NULL,
    `description` VARCHAR(255) DEFAULT NULL,
	`status` ENUM('todo', 'progress', 'done') DEFAULT 'todo',
    `create_datetime` DATETIME DEFAULT NOW(),
	`status_datetime` DATETIME DEFAULT NULL,
    FOREIGN KEY (`board_id`) REFERENCES `boards`(`id`),
    FOREIGN KEY (`tag_id`) REFERENCES `board_tags`(`tag_id`)
);

CREATE TABLE task_comments (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `task_id` INT NOT NULL,
    `text` VARCHAR(300) NOT NULL,
    `created_time` DATETIME NOT NULL DEFAULT NOW(),
    FOREIGN KEY (`task_id`) REFERENCES `board_tasks`(`task_id`)
);
