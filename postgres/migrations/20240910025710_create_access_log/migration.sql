-- CreateTable
CREATE TABLE "access_log" (
    "id" TEXT NOT NULL,
    "request_time" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "access_log_pkey" PRIMARY KEY ("id")
);
