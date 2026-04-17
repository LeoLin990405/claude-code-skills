# Launch Checklist: [Feature/Product Name]

**Launch date**: [Date]
**Launch owner**: [Name]
**Launch type**: Major | Minor | Patch

---

## T-4 Weeks: Planning

### Product
- [ ] PRD approved and signed off
- [ ] Launch criteria defined and agreed
- [ ] Rollout plan finalized (feature flags, % rollout)
- [ ] Rollback criteria defined
- [ ] Success metrics baselined

### Engineering
- [ ] Feature complete
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] Performance benchmarks met
- [ ] Security review completed
- [ ] Monitoring and alerting configured

### Design
- [ ] Final designs reviewed and approved
- [ ] Edge cases covered in design
- [ ] Accessibility audit passed
- [ ] Mobile/responsive verified

---

## T-2 Weeks: Preparation

### QA
- [ ] Test plan created and reviewed
- [ ] Manual QA pass completed
- [ ] Regression testing passed
- [ ] Cross-browser/device testing done
- [ ] Load testing completed (if applicable)

### Documentation
- [ ] Help docs / knowledge base updated
- [ ] API docs updated (if applicable)
- [ ] Internal FAQ for support team prepared
- [ ] Release notes drafted

### Go-to-Market
- [ ] Positioning and messaging finalized
- [ ] Blog post / announcement drafted
- [ ] Email to existing users drafted
- [ ] Social media posts scheduled
- [ ] Sales enablement materials ready (if B2B)
- [ ] Press briefings done (if major launch)

### Support
- [ ] Support team briefed and trained
- [ ] Escalation path defined
- [ ] Known issues documented
- [ ] Response templates prepared for common questions

---

## T-1 Week: Final Prep

### Cross-functional
- [ ] Launch readiness review meeting held
- [ ] All launch criteria met (go/no-go decision)
- [ ] On-call schedule confirmed for launch day
- [ ] Stakeholders notified of launch date
- [ ] Internal demo completed

### Rollout
- [ ] Feature flags configured
- [ ] Dogfood period completed (internal users)
- [ ] Beta users tested (if applicable)
- [ ] Data migration verified (if applicable)
- [ ] Caching / CDN configured

---

## Launch Day

### RACI

| Task | Responsible | Accountable | Consulted | Informed |
|------|------------|-------------|-----------|----------|
| Deploy | [eng] | [eng lead] | [PM] | [team] |
| Monitor metrics | [data/PM] | [PM] | [eng] | [leadership] |
| Publish announcement | [marketing] | [PM] | [design] | [team] |
| Monitor support queue | [support] | [support lead] | [PM] | [team] |
| Rollback decision | [eng lead] | [PM] | [eng] | [leadership] |

### Sequence

- [ ] 09:00 - Final smoke test on staging
- [ ] 09:30 - Deploy to production (X% rollout)
- [ ] 09:45 - Verify core flows working
- [ ] 10:00 - Publish blog post / announcement
- [ ] 10:00 - Send user email
- [ ] 10:15 - Social media posts go live
- [ ] 12:00 - Check metrics (1h post-launch)
- [ ] 14:00 - Check metrics (4h post-launch)
- [ ] 17:00 - End-of-day launch report to stakeholders
- [ ] +1 day - Expand rollout to 50%
- [ ] +3 days - Expand to 100% (if metrics healthy)

---

## Post-Launch: Week 1-4

### Week 1
- [ ] Daily metrics check
- [ ] Triage and fix critical bugs
- [ ] Collect early user feedback
- [ ] Support volume normal (no spike)

### Week 2
- [ ] First metrics review vs. targets
- [ ] User interviews with early adopters (3-5)
- [ ] Address top feedback themes

### Week 4
- [ ] Full metrics review vs. PRD targets
- [ ] Retrospective scheduled and run
- [ ] Learnings documented
- [ ] Next iteration planned (if needed)

---

## Rollback Plan

**Trigger**: [What conditions trigger a rollback]
- [ ] Error rate > [X]%
- [ ] Core flow broken
- [ ] Data integrity issue

**Process**:
1. Disable feature flag
2. Notify stakeholders: [channel/person]
3. Investigate root cause
4. Fix and re-deploy
5. Post-mortem within 48h
