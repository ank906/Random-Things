/**
ok high gamers if u dont know how to do the minecraft tracers thing for 1.12.2 b/c the videos are to hard to find
and well im here to tell u ur dumb and it stupid simple so here:

we put this in renderUtils if u have it
**/
public static void drawTracerLine(double x, double y, double z, float red, float green, float blue, float alpha, float lineWdith) {
	final Minecraft mc = Minecraft.getMinecraft(); 
	final double zerothing = 0.0;
        final Vec3d rotateYaw = new Vec3d(zerothing, zerothing, 1.0).rotatePitch(-(float)Math.toRadians(mc.player.rotationPitch)).rotateYaw(-(float)Math.toRadians(mc.player.rotationYaw));

		GL11.glPushMatrix();
        GL11.glEnable(GL11.GL_BLEND);
        GL11.glEnable(GL11.GL_LINE_SMOOTH);
        GL11.glDisable(GL11.GL_DEPTH_TEST);
        GL11.glDisable(GL11.GL_TEXTURE_2D);
        GL11.glBlendFunc(770, 771);
        GL11.glEnable(GL11.GL_BLEND);
        GL11.glLineWidth(lineWdith);
        GL11.glColor4f(red, green, blue, alpha);
        GL11.glBegin(2);
	//here its the thing under here i wont tell u any more but this make the trachers got to the center of ur thingy
        GL11.glVertex3d(rotateYaw.xCoord, mc.player.getEyeHeight() + rotateYaw.yCoord, rotateYaw.zCoord);
	// oof
        GL11.glVertex3d(x, y, z);
        GL11.glEnd();
        GL11.glDisable(GL11.GL_BLEND);
        GL11.glEnable(GL11.GL_TEXTURE_2D);
        GL11.glEnable(GL11.GL_DEPTH_TEST);
        GL11.glDisable(GL11.GL_LINE_SMOOTH);
        GL11.glDisable(GL11.GL_BLEND);
        GL11.glPopMatrix();
	}
