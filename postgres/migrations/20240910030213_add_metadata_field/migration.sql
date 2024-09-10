-- AlterTable
ALTER TABLE "access_log" ADD COLUMN     "metadata" JSONB NOT NULL DEFAULT '{}';
